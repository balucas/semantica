from flask import Flask
import psycopg2
from flask import request
import os

DB_HOST = os.environ.get('DB_HOST')
DB_PORT = os.environ.get('DB_PORT')
DB_NAME = os.environ.get('DB_NAME')
DB_USER = os.environ.get('DB_USER')
DB_PASSWORD = os.environ.get('DB_PASSWORD')

app = Flask(__name__)

conn = psycopg2.connect(
database=DB_NAME,
user=DB_USER,
password=DB_PASSWORD,
host=DB_HOST, 
port=DB_PORT
)

# Open a cursor to perform database operations
cur = conn.cursor()


@app.route('/')
def hello():
    return "Flask app with PostgreSQL + pgvector"

@app.route('/query', methods=['GET'])
def get_example():
    # For a GET request, data sent by the client is typically in the query string.
    # You can access it using request.args (for URL parameters).
    query_params = request.args  # This is an ImmutableMultiDict of the query parameters
    # Execute a query
    cur.execute("SELECT * FROM user_text")

    # Retrieve query results
    records = cur.fetchall()

    return {
        "received_query_params": query_params.to_dict(),
        "db_query_results": records
            }

@app.route('/upload', methods=['POST'])
def post_example():
    data = request.get_json()
    
    return {"received": data}, 201


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
