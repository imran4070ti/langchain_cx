from langchain_core.output_parsers import JsonOutputParser
from langchain_ollama import ChatOllama
from langchain_core.prompts import PromptTemplate


model = ChatOllama(model='llama3.2:latest')

parser = JsonOutputParser()

template = PromptTemplate(
    template='Write a {character} fiction character\n{structure_format}',
    input_variables=['character'],
    partial_variables={'structure_format' : parser.get_format_instructions()}
)
# print(template)
chain = template | model | parser

result = chain.invoke({'character':'Mobile Man'})

print(result)