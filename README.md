# ⚕️End to End Medical Chatbot 🩺

#### Project Components and Technologies Used
1) OpenAI = LLM
2) Langchain = Orchestration Framework
3) PineCone = Vectordb
4) Flask = Webapp
5) Github = Version controlling
6) AWS = simple deployment and CI/CD deployment

#### We use Pinecone, a cloud-based vector database, to handle the large-scale chunking and storage of a 700-page book, as a local database would be inefficient and lack scalability for this task.

#### Famous LLM ops platforms are aws bedrock and GCP vertex AI


### **Environment Setup**
#### Use python 3.11.4 (Stable)
### **Make sure you have anaconda installed***

0) Clone or download this GitHub repository to your local machine.
1) conda create --name medbot python=3.11.4
2) conda activate medbot
3) pip install -r requirements.txt
4) **Add OpenAI API Key**
   - In the project root, create a `.env` file and add your OpenAI API key in the following format:
     ```
     OPENAI_API_KEY=your_openai_api_key
     ```


Citation : https://www.youtube.com/watch?v=SCZ0BZq-jqY&t=1190s