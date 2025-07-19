from sentence_transformers import SentenceTransformer
from flask import jsonify
model = SentenceTransformer('jinaai/jina-embeddings-v3', trust_remote_code=True)

def embed_text(text):
    embed_vector = model.encode(text)
    return embed_vector.tolist()