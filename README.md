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

<h3>How to Use</h3>

<h6>Clone this repository:</h6>

git clone https://github.com/<your-username>/<your-repo-name>.git
cd <your-repo-name>

<h6>Place the PDF file you want to query in the project directory.</h6>

Update the pdf_path variable in the code to the path of your PDF file:

pdf_path = "./your-file.pdf"  # Replace with your PDF file path

<h6>Run the chatbot:<h6>

python chatbot.py

Enter your queries in the terminal. Type exit to quit the chatbot.

<h3>File Structure</h3>
chatbot.py: The main script for running the chatbot.

requirements.txt: Contains the list of dependencies.

Example PDF files (optional).

<h3>Example Output</h3>

Enter your query (or type 'exit' to quit): What is the main topic of the document?

Most relevant text from the PDF:
This document explains the topic in detail...

<h3>Customization</h3>

Replace the pdf_path variable with the path to your PDF file.

Modify the SentenceTransformer model if needed by changing the initialization line:
