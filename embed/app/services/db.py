import os
import psycopg2
import uuid
from datetime import datetime, timezone
from dotenv import load_dotenv

load_dotenv()
conn = psycopg2.connect(os.getenv("DATABASE_URL"))

### INSERT NOTE ###
def insert_note(user_id, content, embedding, content_format="markdown"):
    note_id = str(uuid.uuid4())
    now = datetime.now(timezone.utc)

    with conn.cursor() as cur:
        # Insert into note_metadata
        cur.execute("""
            INSERT INTO note_metadata (
                id, user_id, date_added, date_updated, content_format, embedding
            ) VALUES (%s, %s, %s, %s, %s, %s)
        """, (
            note_id,
            user_id,
            now,
            now,
            content_format,
            embedding
        ))

        # Insert into note_content with same UUID
        cur.execute("""
            INSERT INTO note_content (note_id, content)
            VALUES (%s, %s)
        """, (
            note_id,
            content
        ))

    conn.commit()
    return note_id


### SEARCH NOTES ###
def search_notes(query_embedding, user_id, limit=5):
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