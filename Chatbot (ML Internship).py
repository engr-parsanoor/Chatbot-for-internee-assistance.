import streamlit as st
from transformers import pipeline

st.set_page_config(page_title="Intern Support Chatbot", page_icon="🤖")
st.title("Intern Support Chatbot 🤖")

qa = pipeline("question-answering", model="distilbert-base-uncased-distilled-squad")

context = """
Interns can request leave through the HR portal.
Internship certificates are issued after successful completion.
For technical issues, email support@company.com.
"""

# simple chat UI
user_input = st.text_input("Ask a question:")

if user_input:
    result = qa(question=user_input, context=context)
    st.markdown(f"**Answer:** {result['answer']}")


