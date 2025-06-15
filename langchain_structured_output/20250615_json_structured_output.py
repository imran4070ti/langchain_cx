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

# json schema
json_schema = {
  "title": "Review",
  "type": "object",
  "properties": {
    "key_themes": {
      "title": "Key Themes",
      "description": "Key things about the review",
      "type": "array",
      "items": {
        "type": "string"
      }
    },
    "summary": {
      "title": "Summary",
      "description": "Summary of the revfiew",
      "type": "string"
    },
    "sentiment": {
      "title": "Sentiment",
      "description": "Sentiment of the review, e.g., positive, negative",
      "type": "string",
      "enum": ["pos", "neg"]
    },
    "pros": {
      "title": "Pros",
      "description": "Pros of the product, if any",
      "type": "array",
      "items": {
        "type": "string"
      }
    },
    "cons": {
      "title": "Cons",
      "description": "Cons of the product, if any",
      "type": "array",
      "items": {
        "type": "string"
      }
    }
  },
  "required": ["key_themes", "summary", "sentiment"]
}

structured_model = model.with_structured_output(json_schema)

response = structured_model.invoke(
    """The refrigerator is great! It keeps my food fresh and has a lot of space. The only downside is that it makes a bit of noise sometimes. Overall, I would recommend it to others.
    Pros: Spacious, keeps food fresh
    Cons: Noisy at times""",
    )

# print(f'Key themes: {response.key_themes}')

# response = dict(response)

print(f"Key themes: {response['key_themes']}")
print(f"Summary: {response['summary']}")
print(f"Sentiment: {response['sentiment']}")
print(f"Pros: {response['pros']}")
print(f"Cons: {response['cons']}")
