from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv
import os

load_dotenv()

model = OpenAIEmbeddings(model='text-embedding-3-small', dimensions=32)

result = model.embed_query('Dhaka is the capital city of Bangladesh.')

print(result)