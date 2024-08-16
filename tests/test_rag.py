
import unittest
from rag_module.rag import RAG
from rag_module.retriever import SimpleRetriever
from rag_module.generator import SimpleGenerator

class TestRAG(unittest.TestCase):
    def test_generate_response(self):
        retriever = SimpleRetriever(config_path="rag_module/config/default_config.yaml")
        generator = SimpleGenerator(model_name="gpt-3.5-turbo")
        rag = RAG(retriever=retriever, generator=generator)
        
        response = rag.generate_response("What is RAG?")
        self.assertIsNotNone(response)

if __name__ == '__main__':
    unittest.main()
