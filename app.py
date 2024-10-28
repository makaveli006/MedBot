from flask import Flask, render_template,jsonify,request
from src.helper import download_hf_embeddings
from langchain_pinecone import PineconeVectorStore
from langchain_openai import OpenAI
from langchain.chains import create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_core.prompts import ChatPromptTemplate
from dotenv import load_dotenv
from src.prompt import *
import os
load_dotenv()
PINECONE_API_KEY = os.environ.get('PINECONE_API_KEY')
os.environ['PINECONE_API_KEY'] = PINECONE_API_KEY
OPENAI_API_KEY = os.environ.get('OPENAI_API_KEY')
os.environ['OPENAI_API_KEY'] = OPENAI_API_KEY

app = Flask(__name__)

embeddings = download_hf_embeddings()

index_name = "medbot"

docsearch = PineconeVectorStore.from_existing_index(
    index_name=index_name,
    embedding=embeddings
)

retriever = docsearch.as_retriever(search_type="similarity",search_kwargs={"k":3})

llm = OpenAI(temperature=0.4,max_tokens=500)

prompt = ChatPromptTemplate.from_messages(
    [
        ("system", system_prompt),
        ("human", "{input}"),
    ]
)

question_answer_chain = create_stuff_documents_chain(llm, prompt)
rag_chain = create_retrieval_chain(retriever, question_answer_chain)

@app.route("/")
def index():
    return render_template('chat.html')

# Chat Operation : If user gives query to chatbot and message is accepted by this endpoint

@app.route("/get",methods=['GET','POST'])
def chat():
    msg=request.form["msg"]
    input = msg
    print(input)
    response = rag_chain.invoke({"input": msg})
    print("Response : ", response['answer'])
    return str(response["answer"])

if __name__ == '__main__':
    app.run(host="0.0.0.0",port=5178,debug=True)