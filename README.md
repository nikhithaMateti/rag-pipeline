<h1>PDF Query Chatbot</h1>

This project implements a chatbot that can answer user queries by finding the most relevant text from a provided PDF file. It uses Natural Language Processing (NLP) techniques and embeddings to compute the similarity between the user query and the PDF content.

<h3>Features</h3>

Extract Text from PDF: Utilizes pdfplumber to extract text from all pages of a PDF file.

Text Embeddings: Leverages the SentenceTransformer library to generate embeddings for the extracted text and user queries.

Query Matching: Computes cosine similarity to identify the most relevant text chunk for a given query.

Interactive Interface: Users can interact with the chatbot through the terminal and receive contextually accurate responses.

<h3>Technologies Used</h3>

Python

pdfplumber for PDF text extraction

sentence-transformers for creating text embeddings

scikit-learn for cosine similarity computation

<h3>Prerequisites</h3>

Python 3.7 or higher

Install the required Python packages:
pip install pdfplumber sentence-transformers scikit-learn
