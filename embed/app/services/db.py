import os
import uuid
from datetime import datetime, timezone
from dotenv import load_dotenv
import psycopg2
from psycopg2.pool import SimpleConnectionPool

load_dotenv()

# Connection pool stuff
DB_URL = os.getenv("DB_URL")

pool = SimpleConnectionPool(minconn=1, maxconn=10, dsn=DB_URL)

def get_conn():
    return pool.getconn()

def release_conn(conn):
    pool.putconn(conn)


def insert_note(user_id, title, content, embedding, content_format="markdown"):
    note_id = str(uuid.uuid4())
    now = datetime.now(timezone.utc)

    conn = get_conn()
    try:
        with conn.cursor() as cur:
            # Insert metadata
            cur.execute("""
                INSERT INTO note_metadata (
                    id, user_id, title, date_added, date_updated, content_format, embedding
                ) VALUES (%s, %s, %s, %s, %s, %s, %s)
            """, (
                note_id,
                user_id,
                title,
                now,
                now,
                content_format,
                embedding
            ))

            # Insert content
            cur.execute("""
                INSERT INTO note_content (note_id, content)
                VALUES (%s, %s)
            """, (
                note_id,
                content
            ))

        conn.commit()
        return note_id

    except Exception as e:
        conn.rollback()
        raise e

    finally:
        release_conn(conn)


def search_notes(query_embedding, user_id, limit=5):
    conn = get_conn()
    try:
        with conn.cursor() as cur:
            cur.execute("""
                SELECT m.id, c.content, 1 - (m.embedding <#> %s::vector) AS score
                FROM note_metadata m
                JOIN note_content c ON m.id = c.note_id
                WHERE m.user_id = %s
                ORDER BY m.embedding <#> %s::vector
                LIMIT %s
            """, (query_embedding, user_id, query_embedding, limit))

            return cur.fetchall()

    finally:
        release_conn(conn)