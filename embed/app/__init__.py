from flask import Flask
from app.routes.embed import embed_bp

def create_app():
    app = Flask(__name__)
    #app.config.from_object("app.config.Config")
    app.register_blueprint(embed_bp)
    return app