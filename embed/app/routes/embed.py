from flask import Blueprint, request, jsonify
from app.services.embedding import embed_text 
from app.services.db import insert_note

embed_bp = Blueprint("embed", __name__)

@embed_bp.route("/embed", methods=["POST"])
def embed():
    print("Received request to /embed")
    data = request.json
    text = data.get("text")
    embedding = embed_text(text)
    print("Generated embedding, length:", len(embedding))
    return jsonify({"embedding": embedding})


@embed_bp.route("/notes", methods=["POST"])
def create_note():
    data = request.get_json()
    embedding = embed_text(data["content"])
    note_id = insert_note(
        title=data["title"],
        content=data["content"],
        user_id=data["user_id"],
        embedding=embedding
    )
    return jsonify({"status": "ok", "note_id": note_id})
