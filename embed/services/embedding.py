from transformers import pipeline

def get_embedding(text):
    print("Generating embedding for text:", text)
    pipe = pipeline(
        "feature-extraction",
        model="jinaai/jina-embeddings-v3",
        trust_remote_code=True
    )
    return pipe(text)