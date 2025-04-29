📝 Project Overview
This project implements an AI-powered chatbot that assists users by answering insurance-related queries based on policy documents.
It leverages Google Gemini API, LangChain, FAISS, and Streamlit to deliver a smart, context-aware conversational experience.
The system retrieves relevant information from a structured PDF-based knowledge base and escalates complex queries to human agents if necessary.

🚀 Key Features
📚 PDF-based Knowledge Base integration.

🧠 Semantic vector search with FAISS for quick document retrieval.

🤖 AI-driven responses using Google Gemini 1.5 Pro model.

💬 Conversation memory management for multi-turn dialogue coherence.

🖥️ Streamlit frontend for easy interaction.

🔄 Fallback mechanism to escalate to human agents when needed.

🎯 Objectives
Implement Natural Language Understanding (NLU) for user queries.

Retrieve accurate information from structured insurance documents.

Manage conversations with context preservation.

Provide a simple and intuitive web interface.

Ensure scalability and high performance under load.

🛠 Technology Stack

Layer	Technology
Language Model (LLM)	Google Gemini API (gemini-1.5-pro)
Embedding Model	HuggingFace all-MiniLM-L6-v2
Vector Store	FAISS (Facebook AI Similarity Search)
Document Loader	LangChain PyPDFLoader
Memory Management	LangChain ConversationBufferMemory
Frontend	Streamlit
Backend/Integration	Python 3

📊 System Architecture
The system includes components for:

User Interface (Streamlit)

Query Processing (Google Gemini)

Knowledge Base Retrieval (FAISS)

Context Management (Conversation Memory)

Fallback to Human Agent

## ▶️ How to Run ##

1. Clone the repository:
   ```bash
   git clone https://github.com/Jxgamessi/AI-POWERED-INSURANCE-CHATBOT.git
   cd AI-POWERED-INSURANCE-CHATBOT
   
2.Install dependencies:

pip install streamlit langchain google-generativeai faiss-cpu sentence-transformers pypdf

3.Important Setup:

>> Open SOURCECODE.py

>> Replace the placeholder Gemini API key with your actual key.

>> Update the knowledge base path according to your local machine folder structure.

4.RUN THE CODE : After updating both the paths and the gemini-api key, RUN the code "SOURCECODE.py".

## 📬 Contact ##

For any queries, please contact: jagatheesvaranx@gmail.com




