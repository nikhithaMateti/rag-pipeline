import pdfplumber
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from sentence_transformers import SentenceTransformer

def extract_text_from_pdf(pdf_path):
    """Extract text from all pages of the PDF."""
    extracted_text = []
    try:
        with pdfplumber.open(pdf_path) as pdf:
            for page_num, page in enumerate(pdf.pages):
                page_text = page.extract_text()
                if page_text:
                    extracted_text.append(page_text)
                    print(f"Extracted text from page {page_num + 1}")
                else:
                    print(f"No text found on page {page_num + 1}")
    except Exception as e:
        print(f"Error while reading PDF: {e}")
    return extracted_text

def create_embeddings(text_chunks, model):
    """Create embeddings for text chunks using a SentenceTransformer model."""
    return model.encode(text_chunks)

def answer_query(query, text_chunks, embeddings, model):
    """Answer a query by finding the most relevant text chunk."""
    query_embedding = model.encode(query)
    similarities = cosine_similarity([query_embedding], embeddings)
    closest_idx = np.argmax(similarities)
    return text_chunks[closest_idx]

# Path to your PDF file
pdf_path = "./r.pdf"  # Change this to your PDF file path

# Initialize the SentenceTransformer model
embedding_model = SentenceTransformer('all-MiniLM-L6-v2')

# Step 1: Extract text from all pages
pdf_text_chunks = extract_text_from_pdf(pdf_path)

if not pdf_text_chunks:
    print("No text found in the PDF.")
else:
    # Step 2: Create embeddings for all text chunks
    pdf_embeddings = create_embeddings(pdf_text_chunks, embedding_model)

    # Step 3: Process user queries
    while True:
        user_query = input("\nEnter your query (or type 'exit' to quit): ").strip()
        if user_query.lower() == 'exit':
            print("Exiting the chatbot. Goodbye!")
            break

        # Step 4: Find the most relevant text and display the answer
        answer = answer_query(user_query, pdf_text_chunks, pdf_embeddings, embedding_model)
        print("\nMost relevant text from the PDF:")
        print(answer)
