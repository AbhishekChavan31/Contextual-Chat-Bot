import pdfplumber
import docx
from typing import List

def parse_pdf(file_path: str) -> str:
    """Extract text from PDF file."""
    text = ""
    with pdfplumber.open(file_path) as pdf:
        for page in pdf.pages:
            text += page.extract_text() + "\n"
    return text

def parse_word(file_path: str) -> str:
    """Extract text from Word file."""
    doc = docx.Document(file_path)
    text = "\n".join([para.text for para in doc.paragraphs])
    return text

def chunk_document(document: str, chunk_size: int = 200) -> List[str]:
    """Split document into chunks of specified size."""
    words = document.split()
    chunks = [" ".join(words[i:i + chunk_size]) for i in range(0, len(words), chunk_size)]
    return chunks