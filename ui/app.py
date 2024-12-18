import streamlit as st
import requests

st.title("Contextual Chatbot")

# Upload document
st.header("Upload Document")
uploaded_file = st.file_uploader("Choose a PDF or Word file", type=["pdf", "docx"])
if uploaded_file is not None:
    with st.spinner("Uploading and processing document..."):
        response = requests.post(
            "http://fastapi:8000/upload",
            files={"file": (uploaded_file.name, uploaded_file, "application/octet-stream")}
        )
        # for render "https://contextual-chat-bot.onrender.com/upload"
        if response.status_code == 200:
            st.success("Document uploaded and processed successfully!")
        # else:
        #     st.error(f"Error: {response.json().get('error')}")

# Query document
st.header("Ask a Question")
question = st.text_input("Enter your question")
if st.button("Get Answer"):
    with st.spinner("Fetching answer..."):
        response = requests.post(
            "http://fastapi:8000/query",
            data={"question": question}
        )
        #for render "https://contextual-chat-bot.onrender.com/query",
        if response.status_code == 200:
            answer = response.json().get("answer")
            st.success(f"Answer: {answer}")
        else:
            st.error(f"Error: {response.json().get('error')}")