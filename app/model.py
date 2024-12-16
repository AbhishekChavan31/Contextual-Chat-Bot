from sentence_transformers import SentenceTransformer

def load_model():
    """Load the SentenceTransformer model."""
    return SentenceTransformer('all-MiniLM-L6-v2')

def generate_embeddings(chunks: list[str], model) -> list:
    """Generate embeddings for chunks."""
    embeddings = model.encode(chunks, convert_to_tensor=True)
    return embeddings