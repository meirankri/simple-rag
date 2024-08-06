# %%
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma
from langchain.text_splitter import RecursiveCharacterTextSplitter

import PyPDF2

def extract_text_from_pdf():
    embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

    # Read the PDF file
    pdf = PyPDF2.PdfReader("genese.pdf")
    pdf_text = ""
    for page in pdf.pages:
        pdf_text += page.extract_text()

    # %%
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    texts = text_splitter.split_text(pdf_text)

    # %%
    vectorstore = Chroma.from_texts(
        texts=texts, 
        embedding= embeddings,
        persist_directory="./db-genese2")

    print("vectorstore created")

