# 🏋️‍♂️ Conversational Q&A Fitness Chatbot  
[![Azure](https://img.shields.io/badge/Azure-OpenAI-blue)](#)  
[![LangChain](https://img.shields.io/badge/LangChain-Orchestration-green)](#)  
[![FAISS](https://img.shields.io/badge/FAISS-Vector%20DB-orange)](#)  
[![Streamlit](https://img.shields.io/badge/Streamlit-UI-red)](#)  
[![Docker](https://img.shields.io/badge/Docker-Containerization-blue)](#)  

## 🔥 Highlights  
- Developed an **AI-powered Conversational Q&A system** for personalized fitness plan and exercise recommendations.  
- Implemented **LangChain orchestration + Azure OpenAI embeddings** for semantic search.  
- Built **FAISS vector index** for fast retrieval and similarity matching.  
- Designed an interactive **Streamlit UI** for user interaction.  
- **Dockerized & deployed** on Azure App Service and published on DockerHub for portability.  

---

## 📖 Features  
✅ Conversational Q&A for fitness & wellness queries  
✅ Personalized recommendations (weight loss, muscle gain, diabetes-friendly, cardio, yoga, etc.)  
✅ **LangChain + Azure OpenAI embeddings** for semantic search  
✅ **FAISS vector store** for fast retrieval  
✅ Interactive **Streamlit UI**  
✅ **Dockerized & deployed** on Azure App Service + DockerHub  

---

## 🛠️ Tech Stack  
- **Azure OpenAI** (text-embedding-3-small)  
- **LangChain**  
- **FAISS**  
- **Streamlit**  
- **Docker**  
- **Azure App Service**  

---

## ⚡ Example Queries  
- *“Show me fitness plans for weight loss with diabetes-friendly meals.”*  
- *“Suggest cardio exercises for someone with heart conditions.”*  
- *“Recommend strength training plans for muscle gain.”*  

---

## 📂 Project Workflow  
1. **Dataset**: Indian fitness & exercise dataset with attributes like age, weight, BMI, health goals, and activity preferences.  
2. **Preprocessing**: Converted dataset rows into text-based documents using **LangChain**.  
3. **Embeddings**: Generated using **Azure OpenAI** and stored locally.  
4. **Vector Search**: Implemented **FAISS index** for semantic retrieval.  
5. **UI**: Built with **Streamlit** for conversational interaction.  
6. **Deployment**: Dockerized and published to **DockerHub** + deployed on **Azure App Service**.  

---

## 🚀 Getting Started  

### 1️⃣ Clone the Repository  
```bash
git clone https://github.com/your-username/fitness-chatbot.git
cd fitness-chatbot
```

### 2️⃣ Install Requirements  
```bash
pip install -r requirements.txt
```

### 3️⃣ Run the App Locally  
```bash
streamlit run app.py
```

### 4️⃣ Docker Setup  
Build and run the container:  
```bash
docker build -t fitness-chatbot .
docker run -p 8501:8501 fitness-chatbot
```

---

---

## 📦 Deployment  
- 🌐 **Azure App Service** – deployed as a cloud-hosted chatbot  
- 🐳 **DockerHub** – [Link to your DockerHub image](https://hub.docker.com/repository/docker/sayedmizan21/fitness_chatbot)  

---

## 🤝 Contribution  
Feel free to fork this repo, raise issues, and submit pull requests.  

---

## 📧 Contact  
👤 **Sayed Mizan Hussain**  
- GitHub: [sayedmizan1](https://github.com/sayedmizan1)  
- LinkedIn: [sayed mizan hussain](https://www.linkedin.com/in/sayed-mizan-hussain-a0133a213/)  
