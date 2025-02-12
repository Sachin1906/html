import streamlit as st
from transformers import pipeline

# Load summarization pipeline
summarizer = pipeline("summarization")

st.title("Legal Document Analysis Tool")

# Upload file
uploaded_file = st.file_uploader("Upload a legal document", type=["txt", "pdf"])

if uploaded_file is not None:
    # Read file content
    text = uploaded_file.read().decode("utf-8")
    
    # Display original text
    st.subheader("Original Document")
    st.write(text)
    
    # Summarize text
    summary = summarizer(text, max_length=500, min_length=25, do_sample=False)
    st.subheader("Summary")
    st.write(summary[0]['summary_text'])
