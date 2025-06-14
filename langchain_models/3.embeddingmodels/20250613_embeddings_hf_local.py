from langchain_huggingface import HuggingFaceEmbeddings
from dotenv import load_dotenv

load_dotenv()

model = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

text = "Dhaka is the capital city of Bangladesh."

results = model.embed_query(text)

print(results)

docs = [
    "Dhaka is the capital city of Bangladesh.",
    "Rangpur is one of the divisional cities of Bangladesh.",
]
results = model.embed_documents(docs)
print(results)