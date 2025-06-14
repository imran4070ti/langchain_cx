from langchain_core.prompts import ChatPromptTemplate

# template = ChatPromptTemplate.from_messages(
template = ChatPromptTemplate([
    ('system', 'You are a {domain} expert.'),
    ('human', 'What is the {topic} in {domain}?')
])

prompt = template.invoke({'domain':'cricket', 'topic':'no ball'})

print(prompt.messages[0].content)
print(prompt.messages[1].content)
