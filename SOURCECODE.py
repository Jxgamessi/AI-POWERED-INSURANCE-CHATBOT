import os
import streamlit as st
import google.generativeai as g
from langchain_community.vectorstores import FAISS
from langchain.embeddings import HuggingFaceEmbeddings
from langchain_community.document_loaders import PyPDFLoader
from langchain.memory import ConversationBufferMemory

#GEMINI API
G = "I WILL BE LEAVING THIS EMPTY, PLEASE REPLACE IT WITH YOUR GOOGLE GEMINI API KEY" #PLEASE SET UP YOUR OWN API KEY,AS DUE TO PRIVACY CONCERNS I CANNOT GIVE IT.
g.configure(api_key=G)

#FUNCTION TO CONVERT PDF TO VECTOR STORES
@st.cache_resource
def l(k):
    d = []
    for p in k:
        l = PyPDFLoader(p)
        docs = l.load()
        d.extend(docs)
    e = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    v = FAISS.from_documents(d, e)
    return v.as_retriever()

#GEMINI RESPONSE
def g_r(q, r, m):
    d = r.get_relevant_documents(q)
    c = "\n\n".join([i.page_content for i in d])
    h = m.buffer_as_messages
    p = f"""
    You are a helpful insurance assistant. Use the following context to answer the question.

    Context:
    {c}

    Chat History:
    {h}

    User Question: {q}

    If you're unsure, respond with: "I'm forwarding your query to a human agent for further assistance."

    Answer:
    """
    mod = g.GenerativeModel("gemini-1.5-pro")
    res = mod.generate_content(p)
    m.save_context({"input": q}, {"output": res.text})
    return res.text

#STREAMLIT-INTERFACE
st.set_page_config(page_title="Insurance Chatbot", layout="centered")
st.title("AI INSURANCE CHATBOT")

#KNOWLEDGE BASE
f = r"C:\Users\rando\OneDrive\Desktop\TCS\KB"
i_t = ["None"] + [f.name for f in os.scandir(f) if f.is_dir()]
t = st.selectbox("Select the insurance type you're interested in:", i_t)


p_f = []
r = None
m = None

#PDF-LOADING
if t != "None":
    s = os.path.join(f, t)
    p_f = [f.path for f in os.scandir(s) if f.is_file() and f.name.endswith('.pdf')]
    
    st.write(f"You selected **{t}** insurance. Please ask your question.")
    u = st.text_input("Ask your insurance-related question")

    if u:
        if p_f:
            with st.spinner(f"Processing {', '.join([os.path.basename(p) for p in p_f])}..."):
                r = l(p_f)
                m = ConversationBufferMemory(return_messages=True)
                st.success(f"✅ {t} insurance policies loaded!")

            with st.spinner("Thinking..."):
                res = g_r(u, r, m)
                st.write("🤖:", res)
        else:
            st.error(f"❌ No PDFs found for the {t} insurance type!")
