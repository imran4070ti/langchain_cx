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

parser = StrOutputParser()

chain = template1 | model | parser | template2 | model | parser

result = chain.invoke({'paper_name' : 'Word2Vec'})

print(result)