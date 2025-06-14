from langchain_ollama import ChatOllama
import streamlit as st

model = ChatOllama(
    model="llama3.1",
    temperature=0.7,
    max_tokens=1000,
    top_p=0.9,
    top_k=50,
)

user_input = st.text_input("Enter your question:", "")

if st.button("Submit"):
    if user_input:
        response = model.invoke(user_input)
        st.write("Response:", response.content)
    else:
        st.write("Please enter a question.")