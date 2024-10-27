# End to End Medical Chatbot

#### We use Pinecone, a cloud-based vector database, to handle the large-scale chunking and storage of a 700-page book, as a local database would be inefficient and lack scalability for this task.

#### Famous LLM ops platforms are aws bedrock and GCP vertex AI

#### In this project
1) OpenAI = LLM
2) Langchain = Orchestration Framework
3) PineCone = Vectordb
4) Flask = Webapp
5) Github = Version controlling
6) AWS = simple deployment and CI/CD deployment


### **Steps to Run 1**

1. **Download the Repository**
   - Clone or download this GitHub repository to your local machine.

2. **Create a Virtual Environment**
   - Run the following command:
     ```bash
     python -m venv venv
     ```

3. **Activate the Virtual Environment**
   - For Linux/macOS:
     ```bash
     source venv/bin/activate
     ```
   - For Windows:
     ```bash
     venv/Scripts/activate
     ```

4. **Install Dependencies**
   - Install all necessary packages by running:
     ```bash
     pip install -r requirements.txt
     ```

5. **Add OpenAI API Key**
   - In the project root, create a `.env` file and add your OpenAI API key in the following format:
     ```
     OPENAI_API_KEY=your_openai_api_key
     ```

6. **Run the Application**
   - Launch the Flask app by executing:
     ```bash
     python app.py
     ```

7. **Access the Application**
   - The app should now be accessible in your web browser. Make sure it is running on a custom port to avoid conflicts with the default localhost port.

8. ### install the requirements
```bash
pip install -r requirements.txt
```
---

### **Additional Notes**

- Ensure that all required permissions and network settings allow for the app to run and retrieve data as needed.
- Review and modify `app.py` if necessary to set a specific port or additional configurations.

---

### **Steps to Run 2**

### **Make sure you have anaconda installed***

1) conda create --name medbot python=3.11.4
2) conda activate medbot
3) ### install the requirements
```bash
pip install -r requirements.txt
```


Citation : https://www.youtube.com/watch?v=SCZ0BZq-jqY&t=1190s