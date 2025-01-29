# HNG12 Stage 0 - Public API

This is a simple **FastAPI-based** public API for **HNG12 Stage 0**. The API provides basic information, including:  

- Your registered **email** (used in the HNG12 Slack workspace).  
- The **current datetime** in ISO 8601 format (UTC).  
- A link to the **GitHub repository** for this project.  

---

## 🚀 Live API URL

> **🔗 [API Base URL](https://your-render-url.onrender.com/)**  

---

## 📌 Features
- **FastAPI-based API** with a simple GET request.  
- Returns JSON response with email, timestamp, and GitHub URL.  
- **CORS support** for accessibility.  
- Deployed on **Render** for public access.  

---

## 🛠️ Setup Instructions (Run Locally)

### **1️⃣ Clone the Repository**
```bash
git clone https://github.com/levoski1/hng12-api.git
cd hng12-api

python3 -m venv venv

- Windows: venv\Scripts\activate
- Mac/Linux: source venv/bin/activate

pip install -r requirements.txt

uvicorn main:app --reload
- The API will be available at http://127.0.0.1:8000/

- URL: https://your-render-url.onrender.com/  (Replace with your actual deployed URL)

```

### **1️⃣ Clone the Repository**