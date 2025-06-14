from langchain_openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

llm = OpenAI(model='gpt-3.5-turbo-instruct')

results = llm.invoke('What is the capital of Bangladesh?')

print(results)