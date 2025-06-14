from langchain_huggingface import ChatHuggingFace, HuggingFacePipeline

llm = HuggingFacePipeline.from_model_id(
    model_id="meta-llama/Meta-Llama-3-8B",
    task="text-generation",
    model_kwargs={"temperature": 0.1, "max_new_tokens": 512}
)
model = ChatHuggingFace(llm=llm)
result = model.invoke('What is the capital of Bangladesh?')
print(result.content)