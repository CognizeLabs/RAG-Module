
# RAG-Module: Retrieval-Augmented Generation in Python

## Overview
The RAG-Module is a Python library designed to simplify the implementation of Retrieval-Augmented Generation (RAG) workflows. This module integrates document retrieval and language generation, allowing you to build powerful AI systems that combine the strengths of both components.

## Features
- **Flexible Retrieval**: Supports integration with various vector databases (e.g., Milvus, FAISS) for efficient document retrieval.
- **Model-Agnostic Generation**: Works with multiple language models (e.g., OpenAI GPT, Hugging Face Transformers).
- **Configurable**: Easy configuration through YAML files to suit different use cases.
- **Extensible**: Designed to be extended with custom retrieval and generation strategies.

## Installation
You can install the library via pip:
```bash
pip install git+https://github.com/CognizeLabs/rag-module.git
```

## Usage
### Basic Example
Here's a simple example to get you started:

```python
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
```

### Advanced Example
For more complex use cases, check out the [examples](examples/advanced_example.py) directory.

## Milvus Integration

The RAG-Module supports Milvus as a vector database for document retrieval.

### Configuration

To use Milvus, set the retriever type to `milvus` in your configuration file:

```yaml
retriever:
  type: 'milvus'
  milvus:
    host: 'localhost'
    port: '19530'
    collection_name: 'your_collection'
    top_k: 5
```

Make sure you have a Milvus server running and your collection is properly set up.

### Example

```python
from rag_module.rag import RAG
from rag_module.retriever import SimpleRetriever
from rag_module.generator import SimpleGenerator

# Initialize retriever with Milvus configuration
retriever = SimpleRetriever(config_path="rag_module/config/default_config.yaml")
generator = SimpleGenerator(model_name="gpt-3.5-turbo")

# Initialize RAG model
rag = RAG(retriever=retriever, generator=generator)

# Perform retrieval-augmented generation
question = "What is Retrieval-Augmented Generation?"
response = rag.generate_response(question)
print(response)
```
