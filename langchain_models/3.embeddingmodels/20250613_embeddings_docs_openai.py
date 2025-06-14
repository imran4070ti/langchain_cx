from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

model = OpenAIEmbeddings(model='text-embedding-3-small', dimensions=32)

docs = [
    'Dhaka is the capital city of Bangladesh.',
    'Rangpur is one of the divisional cities of Bangladesh.',
]

results = model.embed_documents(docs)
print(results)