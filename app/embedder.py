from sentence_transformers import SentenceTransformer
from sentence_transformers.util import cos_sim


model = SentenceTransformer("sentence-transformers/all-MiniLM-L12-v2")

def create_embeddings(texts):
    return model.encode(texts).tolist();
