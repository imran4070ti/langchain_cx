from langchain_core.prompts import MessagesPlaceholder, ChatPromptTemplate

# chat template with message placeholders``
template = ChatPromptTemplate([
    ('system', 'You are a supportive customer service agent.'),
    MessagesPlaceholder(variable_name='chat_history'),
    ('human', '{query}')
])


# load chat history
chat_history = []
with open('langchain_prompts/chat_history.txt', 'r') as file:
    chat_history.extend(file.readlines())


# create prompt
prompt = template.invoke({
    'chat_history': chat_history,
    'query': 'What is the status of my order?'
})


print(prompt)