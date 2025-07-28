import os
from sentence_transformers import SentenceTransformer

model = SentenceTransformer("all-MiniLM-L6-v2")

def embed_query_and_chunks(query, chunks):
    texts = [query] + [c["text"] for c in chunks]
    embeddings = model.encode(texts, convert_to_tensor=False)  # <-- must return NumPy
    return embeddings[0], embeddings[1:]
