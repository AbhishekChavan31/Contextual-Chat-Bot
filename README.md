# End-to-End Contextual Chat Bot Project

This repository contains the implementation of a contextual chatbot capable of reading and processing long documents, answering user queries contextually, and integrating the solution using FastAPI. The project is designed to meet mandatory requirements and tackle advanced challenges, including semantic search and open-source LLM integration.

---

## Project Overview

The contextual chatbot is designed to:
- Parse and process long PDF/Word documents.
- Provide accurate responses to user queries based on document content.
- Integrate with FastAPI for easy deployment and querying.
- Leverage advanced techniques like document chunking and semantic search for improved performance.

---

## Features
- Document parsing for text extraction.
- Contextual query answering.
- Integration with open-source LLMs (e.g., GPT-Neo, LLAMA).
- Semantic similarity search for retrieving relevant document chunks.
- REST API endpoints for document upload and querying.
- Docker-based containerization for simplified deployment.
- MLOps pipeline for monitoring and retraining the model.

---

## Setup Instructions

### Prerequisites
1. Python 3.9 or higher.
2. Virtual environment setup (optional but recommended).
3. Streamlit (for frontend interface).
4. FasAPI (for Backend)
5. Docker (for containerization).

### Installation Steps
1. Clone the repository:
   ```bash
   git clone https://github.com/AbhishekChavan31/qp-ai-assessment.git
   cd qp-ai-assessment
   ```

2. Set up a virtual environment:
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install required Python packages:
   ```bash
   pip install -r requirements.txt
   ```

5. Build and run the application using Docker:
   ```bash
   docker-compose up --build
   ```
   - The `docker-compose.yml` file handles the setup for both the backend (FastAPI) and frontend services.
   - The application will be available at `http://127.0.0.1:8501`.

6. The FastAPI backend is deployed on Render free services, and the Streamlit frontend is publicly 
   accessible at:
   https://contextual-chat-bot-hmqynitngqw8zojbuf5f7a.streamlit.app/
   Note: The response time might be slightly higher due to the free-tier limitations of Render.
   To integrate the frontend with the Render backend:
   * Open the app.py file in the Streamlit frontend codebase.
   * Update the API endpoint to point to the Render backend URL. Replace any local API 
     endpoints with the deployed Render URL, e.g., https://contextual-chat-bot.onrender.com/upload  

---

## Usage Guide

### Upload a Document
1. Use the REST API endpoint `/upload-document` to upload a document.
   - Accepts PDF/Word files.
   - Automatically parses and stores the document for querying.

   Example cURL request:
   ```bash
   curl -X POST "http://127.0.0.1:8000/upload" -F "file=@example.pdf"
   ```

### Query the Chatbot
1. Use the REST API endpoint `/query` to ask questions based on the uploaded document.
   - Provides relevant answers or responds with "I don't know the answer" if no match is found.

   Example cURL request:
   ```bash
   curl -X POST "http://127.0.0.1:8000/query" -H "Content-Type: application/json" -d '{"question": "What is the main topic?"}'
   ```

### Explore Semantic Search
- Retrieve the top 3 most relevant document chunks using semantic similarity.
- Available via the `/query` endpoint.

---

## Technical Details

### Document Parsing
- Extracts text from PDF and Word documents using libraries like PyPDF2 and python-docx.

### Chatbot Architecture
- Built using open-source LLMs (e.g., GPT-Neo or LLAMA).
- Implements context-aware answering using fine-tuned models.

### Semantic Search
- Uses vector databases like Milvus to store and retrieve document chunks based on semantic similarity.

### Docker Integration
- The application is containerized using Docker for easy setup and deployment.
- `docker-compose` is used to orchestrate multi-container setups, including the backend and optional vector database.

### FastAPI Integration
- REST API endpoints for seamless interaction.
- Swagger UI available at `http://127.0.0.1:8000/docs`.

---

## MLOps Pipeline Overview

### Diagram
Include a visual diagram created in draw.io to illustrate the MLOps pipeline:
1. **Data Ingestion:** Document uploads and preprocessing.
2. **Model Training:** Initial training of LLMs with labeled datasets.
4. **Monitoring:** Log responses and track performance metrics.
5. **Retraining:** Schedule periodic retraining with updated data.
6. **Deployment:** Serve the latest model via FastAPI and Docker.

### Key Components
- **Versioning:** Ensure reproducibility and rollback capabilities.
- **Monitoring:** Track user queries and model responses for performance evaluation.
- **Retraining:** Incorporate new data to improve model accuracy.

---

## Contribution Guidelines
1. Fork the repository.
2. Create a feature branch.
3. Submit a pull request for review.

