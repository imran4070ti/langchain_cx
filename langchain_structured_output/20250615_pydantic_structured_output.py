from langchain_ollama import ChatOllama
from typing import TypedDict, Annotated, Optional, List, Literal
from pydantic import BaseModel, Field


model = ChatOllama(
    model="llama3.2:latest",
    temperature=0.7,
    max_tokens=1000,
    top_p=0.9,
    top_k=50,
)

class Review(BaseModel):
    key_themes: List[str] = Field(description='Key things about the review')
    summary: str = Field(description='Summary of the revfiew')
    sentiment: Literal['pos', 'neg'] = Field(description='Sentiment of the review, e.g., positive, negative')
    pros: Optional[list[str]] = Field(description='Pros of the product, if any') 
    cons: Optional[list[str]] = Field(description='Cons of the product, if any') 

structured_model = model.with_structured_output(Review)

response = structured_model.invoke(
    """The refrigerator is great! It keeps my food fresh and has a lot of space. The only downside is that it makes a bit of noise sometimes. Overall, I would recommend it to others.
    Pros: Spacious, keeps food fresh
    Cons: Noisy at times""",
    )

print(f'Key themes: {response.key_themes}')

response = dict(response)

print(f"Key themes: {response['key_themes']}")
print(f"Summary: {response['summary']}")
print(f"Sentiment: {response['sentiment']}")
print(f"Pros: {response['pros']}")
print(f"Cons: {response['cons']}")