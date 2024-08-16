
from rag_module.retriever import SimpleRetriever
from rag_module.generator import SimpleGenerator

class RAG:
    def __init__(self, retriever, generator):
        self.retriever = retriever
        self.generator = generator

    def generate_response(self, query):
        documents = self.retriever.retrieve(query)
        combined_context = " ".join([doc['content'] for doc in documents])
        response = self.generator.generate(combined_context)
        return response
