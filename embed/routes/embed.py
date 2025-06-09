from flask import Blueprint, request, jsonify
from services.embedding import get_embedding

embed_bp = Blueprint("embed", __name__)

@embed_bp.route("/embed", methods=["POST"])
def embed():
    print("Received request to /embed")
    data = request.json
    text = data.get("text")
    embedding = get_embedding(text)
    print("Generated embedding, length:", len(embedding))
    return jsonify({"embedding": embedding})