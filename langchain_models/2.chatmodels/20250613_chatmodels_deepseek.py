from langchain_deepseek import ChatDeepSeek
from dotenv import load_dotenv
import os

load_dotenv()

model = ChatDeepSeek(model='deepseek-chat')

result = model.invoke('What is the capital of Bangladesh?')
print(result)