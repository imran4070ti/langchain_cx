from langchain_core.messages import HumanMessage, SystemMessage, AIMessage
from langchain_ollama import ChatOllama

model = ChatOllama(model="llama3.1")

messages = [
    SystemMessage(content="You are a helpful assistant."),
    HumanMessage(content="What is LangChain?")
]

response = model.invoke(messages)

messages.append(response.content)

print(messages)