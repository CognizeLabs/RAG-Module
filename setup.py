
from setuptools import setup, find_packages

setup(
    name='rag-module',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'pymilvus==2.2.0',
        'openai==0.27.0',
        'pydantic==1.10.2',
        'pyyaml==6.0'
    ],
    author='Your Name',
    author_email='your.email@example.com',
    description='A Python library for Retrieval-Augmented Generation (RAG).',
    url='https://github.com/yourusername/rag-module',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)
