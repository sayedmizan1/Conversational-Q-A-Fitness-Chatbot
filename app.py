from langchain_community.vectorstores import FAISS
import warnings
warnings.filterwarnings('ignore')
from langchain_openai import AzureOpenAIEmbeddings
import os
from langchain.chains import RetrievalQA
from openai import AzureOpenAI
from langchain.chat_models import AzureChatOpenAI
import streamlit as st
 
print('Hello')
endpoint =  os.getenv("AZURE_OPENAI_ENDPOINT")
deployment = os.getenv("DEPLOYMENT_NAME", "gpt-4.1-nano")
subscription_key = os.getenv("AZURE_OPENAI_API_KEY")
 
# Initialize Azure OpenAI client with key-based authentication
client = AzureOpenAI(
    azure_endpoint=endpoint,
    api_key=subscription_key,
    api_version="2025-01-01-preview",
)
 
llm = AzureChatOpenAI(
    azure_deployment=deployment,
    azure_endpoint=endpoint,
    openai_api_key=subscription_key,
    api_version="2024-12-01-preview", # Added api_version
    temperature=0.7,
    max_tokens=1000
)
 
azure_embeddings = AzureOpenAIEmbeddings(
    azure_deployment="text-embedding-3-large",
    model="text-embedding-3-large",
    api_key=subscription_key, # Replace with your actual API key or use environment variables/secrets
    azure_endpoint=endpoint,
    api_version="2024-12-01-preview",
)
 
loaded_faiss_store = FAISS.load_local("Fitness",embeddings=azure_embeddings, allow_dangerous_deserialization=True)
print("FAISS index loaded from 'faiss_vectorstore'")
 
Retrieval_chain = RetrievalQA.from_chain_type(llm=llm, retriever=loaded_faiss_store.as_retriever(), return_source_documents=True)
 
st.title("Fitness AI Assistant")
 
if "messages" not in st.session_state:
    st.session_state.messages = []
 
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])
 
if prompt := st.chat_input("Ask me anything..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)
 
    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        full_response = ""
        reply = Retrieval_chain(prompt)
        full_response = reply['result']
        message_placeholder.markdown(full_response)
    st.session_state.messages.append({"role": "assistant", "content": full_response})