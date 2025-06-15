from langchain_core.output_parsers import StrOutputParser
from langchain_ollama import ChatOllama
from langchain_core.prompts import PromptTemplate

model = ChatOllama(model='llama3.2:latest')

# First template
template1 = PromptTemplate(
    template = 'Explain the paper {paper_name} in details',
    input_variables=['paper_name']
)

# Second template
template2 = PromptTemplate(
    template='Summarize the following text in 5 lines.\n{text}',
    input_variables=['text']
)

prompt1 = template1.invoke({
    'paper_name' : 'Word2Vec'
})

response1 = model.invoke(prompt1)

prompt2 = template2.invoke({
    'text':response1.content
})

response2 = model.invoke(prompt2)

print(response1.content)
print('*****************************')
print(response2.content)