
from rag_module.rag import RAG
from rag_module.retriever import SimpleRetriever
from rag_module.generator import SimpleGenerator

# Initialize retriever and generator
retriever = SimpleRetriever(config_path="rag_module/config/default_config.yaml")
generator = SimpleGenerator(model_name="gpt-3.5-turbo")

# Initialize RAG model
rag = RAG(retriever=retriever, generator=generator)

# Perform retrieval-augmented generation
question = "What is Retrieval-Augmented Generation?"
response = rag.generate_response(question)
print(response)
