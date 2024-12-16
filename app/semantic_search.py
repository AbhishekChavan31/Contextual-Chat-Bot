from sentence_transformers import util
import numpy as np

def semantic_search(query: str, chunks: list[str], embeddings, model) -> str:
    """Retrieve the most relevant chunk for a query."""
    query_embedding = model.encode(query, convert_to_tensor=True)
    similarities = util.cos_sim(query_embedding, embeddings)
    similarities = similarities.cpu().numpy()
    top_match_idx = int(np.argmax(similarities))
    if similarities[0][top_match_idx] < 0.2:  # Confidence threshold
        return "I don't know the answer."
    # Extract the top-matching chunk
    top_chunk = chunks[top_match_idx]
    
    # Convert text to pointwise format
    points = top_chunk.split("\n")  # Split by newlines for a basic pointwise structure
    formatted_answer = "\n".join(f"- {point.strip()}" for point in points if point.strip())
    
    return formatted_answer