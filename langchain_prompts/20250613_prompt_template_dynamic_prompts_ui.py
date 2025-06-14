from langchain_ollama import ChatOllama
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import streamlit as st
from langchain_core.prompts import PromptTemplate, load_prompt

load_dotenv()


model = ChatOllama(
    model="llama3.1",
    temperature=0.7,
    max_tokens=1000,
    top_p=0.9,
    top_k=50,
)

# model = ChatOpenAI(model="gpt-4o")

st.header("Research Tool")

paper_input = st.text_input("Enter the paper title:", "")
style_input = st.selectbox("Select explanation style:", ["Simple", "Detailed", "Technical"])
length_input = st.selectbox("Select response length:", ["Short", "Medium", "Long"])

# template
# template = PromptTemplate(
#     template = '''
#         You are an expert in explaining research papers. Your task is to provide a clear and concise explanation of the paper titled "{paper_input}" in a {style_input} style with a {length_input} response.
#         Ensure that the summary is clear, informative, and tailored to the selected style and length.
#     ''',
#     input_variables=["paper_input", "style_input", "length_input"]
# )
# template.save('langchain_prompts/template.json')

# Reusing the saved template
template = load_prompt('langchain_prompts/template.json')

# prompt = template.invoke(
#     {
#         'paper_input': paper_input,
#         'style_input': style_input,
#         'length_input': length_input
#     }
# )

if st.button("Submit"):
    chain = template | model
    if paper_input:
        
        # response = model.invoke(prompt)
        response = chain.invoke(
            {
                'paper_input': paper_input,
                'style_input': style_input,
                'length_input': length_input
            }
        )
        st.write("Response:", response.content)
    else:
        st.write("Please enter a paper title.")
# Add a footer with a link to the GitHub repository