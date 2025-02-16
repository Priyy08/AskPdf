import os
from dotenv import load_dotenv
import streamlit as st
from PyPDF2 import PdfReader
from langchain.text_splitter import CharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain.chains.question_answering import load_qa_chain
from langchain_community.llms import HuggingFaceEndpoint
from langchain import HuggingFaceHub

# Load environment variables
load_dotenv()
api_token = os.getenv("HUGGINGFACEHUB_API_TOKEN")

# Streamlit configuration
st.set_page_config(page_title="Ask your PDF")
st.header("Ask Your PDF")

# File uploader
pdf = st.file_uploader("Upload your pdf", type="pdf")

if pdf is not None:
    pdf_reader = PdfReader(pdf)
    text = ""
    for page in pdf_reader.pages:
        text += page.extract_text()

    # Split text into chunks
    text_splitter = CharacterTextSplitter(
        separator="\n",
        chunk_size=1000,
        chunk_overlap=200,
        length_function=len
    )
    chunks = text_splitter.split_text(text)

    # Create embedding
    embeddings = HuggingFaceEmbeddings()

    # Create knowledge base
    knowledge_base = FAISS.from_texts(chunks, embeddings)

    # User question input
    user_question = st.text_input("Ask Question about your PDF:")
    if user_question:
        docs = knowledge_base.similarity_search(user_question)
        llm = HuggingFaceHub(repo_id="google/flan-t5-large", model_kwargs={"temperature": 1.0, "max_length": 256})

        chain = load_qa_chain(llm, chain_type="stuff")
        response = chain.run(input_documents=docs, question=user_question)

        st.write(response)
