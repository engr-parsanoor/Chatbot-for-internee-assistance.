Intern Support Chatbot 🤖

This is a basic Question Answering (QA) chatbot developed using Streamlit and Hugging Face Transformers. It was built as part of my internship at Internee.pk
.

🔍 Project Details

The chatbot is designed to answer interns’ common questions from a fixed context. It uses DistilBERT, a lightweight Transformer model, fine-tuned on the SQuAD dataset.

Frontend/UI → Built with Streamlit

Backend Model → Hugging Face pipeline("question-answering")

Context → Predefined text containing internship-related information

Output → Extracted answer from context based on user’s query

🛠 Code Explanation
import streamlit as st
from transformers import pipeline

# Streamlit page setup
st.set_page_config(page_title="Intern Support Chatbot", page_icon="🤖")
st.title("Intern Support Chatbot 🤖")

# Load Hugging Face Question Answering pipeline
qa = pipeline("question-answering", model="distilbert-base-uncased-distilled-squad")

# Predefined context for answering questions
context = """
Interns can request leave through the HR portal.
Internship certificates are issued after successful completion.
For technical issues, email support@company.com.
"""

# User input field
user_input = st.text_input("Ask a question:")

# Generate answer if user enters a question
if user_input:
    result = qa(question=user_input, context=context)
    st.markdown(f"**Answer:** {result['answer']}")

🔎 Line by Line Explanation

st.set_page_config & st.title → Sets up chatbot’s UI in Streamlit.

pipeline("question-answering") → Loads a pretrained QA model.

context → Acts as the knowledge base of the chatbot.

st.text_input → Takes user’s question as input.

qa(question=user_input, context=context) → Runs QA model to find the answer.

st.markdown → Displays the model’s answer on the UI.
🎯 Learning Outcomes

How to integrate NLP models into web apps.

Basics of Streamlit UI for ML projects.

Understanding of Question Answering pipeline using Transformers.

🙌 Acknowledgment

This project was created as my final internship task at Internee.pk, Pakistan’s leading remote internship platform. The platform gave me the opportunity to explore practical AI projects, improve my skills, and gain confidence in applying ML concepts.
