from langchain_ollama import ChatOllama
from langchain_core.messages import HumanMessage, SystemMessage, AIMessage

model = ChatOllama(model="llama3.1")

chat_history = [SystemMessage(content='You are a helpful assistant.')]

while True:
    user_input = input('You: ')
    if user_input.lower() in ['exit', 'quit']:
        print("Exiting the chatbot.")
        break
    chat_history.append(HumanMessage(content=user_input))

    response = model.invoke(chat_history)
    print(f'Assistant: {response.content}')

    chat_history.append(AIMessage(content=response.content))

print(f'Chat history: {chat_history}')
