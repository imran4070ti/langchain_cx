from langchain_ollama import ChatOllama
from typing import TypedDict, Annotated, Optional


model = ChatOllama(
    model="llama3.1",
    temperature=0.7,
    max_tokens=1000,
    top_p=0.9,
    top_k=50,
)

class Review(TypedDict):
    key_themes: Annotated[list[str], 'Key things about the review']
    summary: Annotated[str, 'Summary of the review']
    sentiment: Annotated[str, 'Sentiment of the review, e.g., positive, negative, neutral']
    pros: Annotated[Optional[list[str]], 'Pros of the product, if any'] 
    cons: Annotated[Optional[list[str]], 'Cons of the product, if any']

structured_model = model.with_structured_output(Review)

response = structured_model.invoke(
    """The refrigerator is great! It keeps my food fresh and has a lot of space. The only downside is that it makes a bit of noise sometimes. Overall, I would recommend it to others.
    Pros: Spacious, keeps food fresh
    Cons: Noisy at times""",
    )
print(f"Key themes: {response['key_themes']}")
print(f"Summary: {response['summary']}")
print(f"Sentiment: {response['sentiment']}")
print(f"Pros: {response['pros']}")
print(f"Cons: {response['cons']}")