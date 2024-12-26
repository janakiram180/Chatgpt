

# ChatGPT Document Q&A Bot  

This repository contains a chatbot application that integrates **ChatGPT** with a **vector database** to provide intelligent and context-aware answers to user queries based on stored documents.  

## Features  
- **ChatGPT Integration**: Leverages the capabilities of ChatGPT for natural language understanding and response generation.  
- **Document-Based Q&A**: Answers questions using documents stored in a vector database for enhanced accuracy and relevance.  
- **Vector Search**: Efficiently retrieves the most relevant document segments for user queries.  
- **LangChain Integration**: Employs LangChain tools for seamless interaction between ChatGPT and the vector database.  

## How It Works  
1. **Document Upload**: Documents are indexed and stored in a vector database.  
2. **Query Input**: The user inputs a question via the chatbot interface.  
3. **Vector Search**: The query is matched against stored documents to retrieve relevant context.  
4. **Response Generation**: ChatGPT uses the retrieved context to generate precise answers.  

## Requirements  
- Python 3.8+  
- Libraries:  
  - `langchain`  
  - `openai`  
  - `faiss` or another vector database library  
  - `streamlit` (optional for building a web interface)  

## Setup Instructions  
1. Clone the repository:  
   ```bash  
   git clone https://github.com/janakiram180/Chatgpt.git  
   cd Chatgpt  
   ```  
2. Install dependencies:  
   ```bash  
   pip install -r requirements.txt  
   ```  
3. Set up your OpenAI API key:  
   - Create a `.env` file and add your API key:  
     ```  
     OPENAI_API_KEY=your_openai_api_key  
     ```  
4. Run the chatbot application:  
   ```bash  
   python app.py  
   ```  

## Usage  
- Upload your documents to the vector database.  
- Start a conversation with the chatbot and ask questions related to the uploaded documents.  
- The bot will retrieve relevant information and provide accurate answers.  

## Technologies Used  
- **ChatGPT**: For natural language processing and response generation.  
- **LangChain**: To streamline the interaction between ChatGPT and the vector database.  
- **Vector Database**: For efficient document retrieval.  
- **Python**: Backend implementation.  

## Future Enhancements  
- Add support for multiple vector database backends.  
- Improve response accuracy with better fine-tuning of document search parameters.  
- Create a web-based interface for enhanced user experience.  

## License  
This project is licensed under the MIT License. See the `LICENSE` file for more details.  

