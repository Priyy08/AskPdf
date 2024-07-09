# Ask Your PDF with Streamlit and Hugging Face

This project demonstrates a Streamlit application that allows users to upload a PDF document, extract text from it, create embeddings using Hugging Face, and perform question-answering on the extracted text chunks.

## Features

- **PDF Upload:** Users can upload a PDF document.
- **Text Extraction:** Extracts text from the uploaded PDF.
- **Text Chunking:** Splits the extracted text into manageable chunks.
- **Embeddings:** Uses Hugging Face embeddings to create representations of text chunks.
- **Knowledge Base:** Constructs a knowledge base using FAISS from the text chunks.
- **Question Answering:** Allows users to input a question about the PDF content and retrieves relevant answers using a Hugging Face language model.

## Prerequisites

- Python 3.12.0 installed on your system.
- pip package manager installed.

## Installation

1. Clone the repository:
   
   git clone https://github.com/Priyy08/AskPdf.git


3. Install dependencies:
   pip install -r requirements.txt

## Setup

1. **Environment Variables:**
   
   Make an account on huggingface.com and get your HuggingFace API token from settings panel.

   Make sure to set up a `.env` file in the root directory of your project with the following content:

   HUGGINGFACEHUB_API_TOKEN=your_huggingfacehub_api_token_here

   Replace `your_huggingfacehub_api_token_here` with your actual Hugging Face Hub API token.

1. **Run the Application:**

   Start the Streamlit application:
   
   streamlit run askpdf.py

## Usage

1. Open the Streamlit app in your web browser using streamlit run askpdf.py command.
2. Upload a PDF file using the file uploader.
3. Once uploaded, ask a question related to the content of the PDF.
4. The application will process the text, generate embeddings, perform a similarity search, and provide an answer to your question based on the extracted knowledge.

