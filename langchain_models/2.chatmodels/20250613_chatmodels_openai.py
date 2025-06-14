from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import os

load_dotenv()


model = ChatOpenAI(model='gpt-4.1-nano') # temperature - is a parameter that controls the randomness of the output. Lower values make the output more deterministic.
results = model.invoke('What is the capital of Bangladesh?')

print(results.content)