
from pymilvus import Collection, connections
from rag_module.config import ConfigLoader

class SimpleRetriever:
    def __init__(self, config_path):
        config = ConfigLoader.load_config(config_path)
        self.retriever_type = config['retriever']['type']
        
        if self.retriever_type == 'milvus':
            self._setup_milvus(config['retriever']['milvus'])

    def _setup_milvus(self, milvus_config):
        connections.connect(alias="default", host=milvus_config['host'], port=milvus_config['port'])
        self.collection = Collection(milvus_config['collection_name'])
        self.top_k = milvus_config['top_k']

    def retrieve(self, query):
        if self.retriever_type == 'milvus':
            return self._milvus_retrieve(query)
        else:
            return [{'content': 'Sample document content'}]

    def _milvus_retrieve(self, query):
        vector = self._get_query_embedding(query)
        search_params = {"metric_type": "L2", "params": {"nprobe": 10}}
        results = self.collection.search([vector], "embeddings", search_params, limit=self.top_k)

        documents = []
        for result in results[0]:
            documents.append({'content': result.entity.get('content')})
        
        return documents

    def _get_query_embedding(self, query):
        return [0.1] * 128  # Example embedding vector
