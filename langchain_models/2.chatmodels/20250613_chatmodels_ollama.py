from langchain_ollama import ChatOllama

model = ChatOllama(model="llava:34b")

result = model.invoke('What is the capital of Bangladesh?')
print(result.content)