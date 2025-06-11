from app import create_app
from os import environ

app = create_app()

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=int(environ.get('PORT', 5001)))
