import os
import pandas as pd
import time
from dotenv import load_dotenv
from langchain_openai import AzureOpenAIEmbeddings
from langchain_community.vectorstores import FAISS
from langchain.schema import Document
from langchain_community.document_loaders import CSVLoader
# -------------------------------
# Load environment variables
# -------------------------------
load_dotenv()

azure_endpoint = os.getenv("AZURE_OPENAI_ENDPOINT")
azure_api_key = os.getenv("AZURE_OPENAI_API_KEY")
embedding_deployment = os.getenv("AZURE_EMBEDDING_DEPLOYMENT")  # "text-embedding-3-large"
azure_api_version = os.getenv("AZURE_OPENAI_API_VERSION", "2025-01-01-preview")

# -------------------------------
# Create Embedding Model with rate limiting
# -------------------------------
embeddings = AzureOpenAIEmbeddings(
    azure_endpoint=azure_endpoint,
    azure_deployment=embedding_deployment,
    openai_api_key=azure_api_key,
    api_version=azure_api_version,
    max_retries=5,  # Retry failed requests
    request_timeout=60,  # Timeout for requests
    chunk_size=100,  # Process documents in batches of 100
)

# -------------------------------
# Load CSV and Excel Files
# -------------------------------
docs = []

# Load gym.csv
if os.path.exists("gym_members_exercise_tracking.csv"):
    df_gym = pd.read_csv("gym_members_exercise_tracking.csv")
    for _, row in df_gym.iterrows():
        text = " ".join([f"{col}: {row[col]}" for col in df_gym.columns if pd.notna(row[col])])
        docs.append(Document(page_content=text))

if os.path.exists("megaGymDataset.csv"):
    df_gymdataset = pd.read_csv("megaGymDataset.csv")
    for _, row in df_gymdataset.iterrows():
        text = " ".join([f"{col}: {row[col]}" for col in df_gymdataset.columns if pd.notna(row[col])])
        docs.append(Document(page_content=text))

# Load the preprocessed chunked data using CSVLoader
loader = CSVLoader(file_path='Datasets/preprocessed_chunked_data.csv', encoding='utf-8')
data = loader.load()
 
 

print(f"Loaded {len(docs)} documents from gym.csv and diet.xlsx")

# -------------------------------
# Build FAISS Index
# -------------------------------
faiss_store = FAISS.from_documents(data, embedding=embeddings)

# Save index to 'Fitness' folder
faiss_store.save_local("Fitness")

print("FAISS index built successfully with your documents (text-embedding-3-large)")
