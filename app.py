from langchain_community.vectorstores import Chroma
from langchain.prompts import ChatPromptTemplate
from langchain.schema.runnable import RunnablePassthrough
from langchain_huggingface import HuggingFaceEmbeddings
from dotenv import load_dotenv
import os
from langchain_groq import ChatGroq

# Load environment variables
load_dotenv()
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

# Initialize embeddings and database
embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
db = Chroma(persist_directory="./db-genese2", embedding_function=embeddings)

# Create retriever
retriever = db.as_retriever(search_type="similarity", search_kwargs={"k": 5})

# Initialize the language model
llm = ChatGroq(model="llama3-8b-8192")

# Create prompt template
template = """<bos><start_of_turn>user\nAnswer the question based only on the following context and extract out a meaningful answer. \
Please write in full sentences with correct spelling and punctuation. if it makes sense use lists. \
If the context doesn't contain the answer, just respond that you are unable to find an answer. \
Use the question language to respond if the question is in french respond in french same for english or hebrew.  \
Answer in the same language as the question. \
If the question is too vague, respond with "The question is too vague". \
If the question is too complex, respond with "The question is too complex". \
 
CONTEXT: {context}

QUESTION: {question}

<end_of_turn>
<start_of_turn>model\n
ANSWER:"""

prompt = ChatPromptTemplate.from_template(template)

# Define the RAG chain
rag_chain = (
    {"context": retriever, "question": RunnablePassthrough()}
    | prompt
    | llm
)

def ask_question(question):
    responses = []
    for chunk in rag_chain.stream(question):
        responses.append(chunk.content)
    return "".join(responses)

# Example usage



from flask import Flask, jsonify, request
from embedding import extract_text_from_pdf

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False  # Assure que JSON utilise UTF-8

@app.route('/')
def home():
    return jsonify({"message": "Accents: éàè"})

@app.route('/question', methods=['GET'])
def transform_text():
    # Récupérer le texte du paramètre d'URL 'text'
    text = request.args.get('question', '')
    response = ask_question(text)
    # Transformer le texte en majuscules

    # Retourner le texte transformé
    return jsonify({"question": text, "answer": response})

@app.route('/api/data')
def data():
    extract_text_from_pdf()
    return jsonify({"data": [1, 2, 3, 4, 5]})

if __name__ == '__main__':
    app.run(debug=True)
