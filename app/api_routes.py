from fastapi import APIRouter, UploadFile, Form
from fastapi.responses import JSONResponse
import os
from prprocessing import parse_pdf, parse_word, chunk_document
from model import load_model, generate_embeddings
from semantic_search import semantic_search

router = APIRouter()

# Globals to store chunks and embeddings
stored_chunks = []
stored_embeddings = None
model = load_model()

@router.post("/upload")
async def upload_document(file: UploadFile):
    """Upload and process a document."""
    try:
        file_path = f"temp_{file.filename}"
        with open(file_path, "wb") as f:
            f.write(file.file.read())
        if file.filename.endswith(".pdf"):
            document = parse_pdf(file_path)
        elif file.filename.endswith(".docx"):
            document = parse_word(file_path)
        else:
            return JSONResponse(content={"error": "Unsupported file format."}, status_code=400)

        os.remove(file_path)  # Clean up uploaded file

        global stored_chunks, stored_embeddings
        stored_chunks = chunk_document(document)
        stored_embeddings = generate_embeddings(stored_chunks, model)

        return JSONResponse(content={"message": "Document uploaded and processed successfully."}, status_code=200)

    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=500)

@router.post("/query")
async def query_document(question: str = Form(...)):
    """Query the document for an answer."""
    try:
        if not stored_chunks:
            return JSONResponse(content={"error": "No document uploaded."}, status_code=400)
        answer = semantic_search(question, stored_chunks, stored_embeddings, model)
        return JSONResponse(content={"answer": answer}, status_code=200)

    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=500)