from flask import Flask
import psycopg2
from flask import request, render_template
import os
from assert_data import assert_upload
import numpy as np
import datetime

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


def get_embedding(text, n=3):
    embedding = np.random.rand(n)
    
    return embedding.tolist()
    
def insert_with_vec(data): #TODO: make this support batch operations
    '''
    Inserts a user's text along with a vector embedding
    
    Parameters:
    data: response body object containing user's data
    
    '''
    user = data['username']
    userid = np.random.randint(1000,1100)
    actual_data_nocontext = data['actual_data']
    embedding = get_embedding(actual_data_nocontext, n=3)
    date_added = datetime.datetime.now()
    
    # Get format information
    validation_result = assert_upload(data)
    format_type = validation_result['format']
    
    with conn.cursor() as cur:
        cur.execute('''INSERT INTO user_text 
                    (user_id, embedding, date_added, content, format_type) 
                    VALUES (%s, %s, %s, %s, %s)''', 
                    (userid, embedding, date_added, actual_data_nocontext, format_type))
        conn.commit()
    
@app.route('/')
def hello():
    return render_template('index.html')

@app.route('/query', methods=['GET'])
def get_example():
    query_params = request.args
    
    with conn.cursor() as cur:
        cur.execute("SELECT * FROM user_text")
        records = cur.fetchall()

    return {
        "received_query_params": query_params.to_dict(),
        "db_query_results": records
            }

@app.route('/upload', methods=['POST'])
def post_example():
    try:
        data = request.get_json()
        if not data:
            return {"error": "No JSON data provided"}, 400
            
        validation_result = assert_upload(data)
        insert_with_vec(data)
        
        return {
            "status": "success",
            "message": "Data uploaded successfully",
        }, 201
        
    except ValueError as e:
        return {"error": str(e)}, 400
    except Exception as e:
        return {"error": f"An unexpected error occurred: {str(e)}"}, 500


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
