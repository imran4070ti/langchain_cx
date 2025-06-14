from langchain_huggingface import HuggingFaceEmbeddings
from sklearn.metrics.pairwise import cosine_similarity

model = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

docs = [
    'Dhaka is the capital city of Bangladesh.',
    'Rangpur is one of the divisional cities of Bangladesh.',
    'Chittagong is a major port city in Bangladesh.',
    'Sylhet is known for its tea gardens and natural beauty.',
    'Khulna is famous for the Sundarbans mangrove forest.',
    'Rajshahi is known for its silk and mangoes.',
    'Barisal is known for its rivers and waterways.',
    'Comilla is known for its historical sites and educational institutions.',
    'Narayanganj is an industrial city near the capital.',
    'Gazipur is an industrial city near Dhaka.',
    'Mymensingh is known for its educational institutions and culture.',
    'Jessore is known for its agriculture and trade.',
    'Pabna is known for its agriculture and historical significance.',
    'Bogra is known for its agriculture and trade.',
    'Tangail is known for its handloom products and textiles.',
    'Cox\'s Bazar is famous for having the longest natural sea beach in the world.',
]

doc_embeddings = model.embed_documents(docs)


query = input('Query: ')
# query = 'Tell me about Rangpur city'
query_embedding = model.embed_query(query)

results = cosine_similarity([query_embedding], doc_embeddings)[0]

index, score = sorted(list(enumerate(results)), key=lambda x: x[1], reverse=True)[0]

print(f'Ans: {docs[index]}')
print(f'Score: {score:.4f}')