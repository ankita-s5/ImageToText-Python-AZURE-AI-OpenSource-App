# 🖼️ ImageToText – Python Azure AI Open Source App

## 📌 Project Overview
**ImageToText – Python Azure AI Open Source App** is an open-source application that extracts text from images using **Microsoft Azure AI services**.
This project demonstrates how to integrate **Azure Cognitive Services (Computer Vision / OCR)** with Python to build a scalable, cloud-ready AI solution.

---

## 🎯 Key Features
- 📸 Text extraction using **Azure AI Vision OCR**
- ☁️ Cloud-based AI (no local OCR engine required)
- 🔍 Supports printed and handwritten text
- ⚡ High accuracy with Azure Cognitive Services
- 📄 Export extracted text
- 🧩 Enterprise-ready architecture

---

## 🧠 Skills Demonstrated
- Azure Cognitive Services
- Python Azure SDK
- REST API consumption
- Secure credential handling
- Computer Vision & OCR
- Open-source best practices

---

## 🛠 Tech Stack
- **Language:** Python  
- **Cloud AI:** Azure AI Vision  
- **Libraries:** azure-ai-vision, requests, Pillow, NumPy  

---

## ☁️ Azure Services Used
- Azure AI Vision
- Azure Cognitive Services

---

## 📂 Project Structure
```text
ImageToText-Python-AZURE-AI-OpenSource-App/
│
├── images/
│   └── 1.png
│
├── src/
│   ├── read-text.py
│   └── .env
│
├── output/
│   └── 
│
└── README.md
```

---

## ▶️ How to Run

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/ankita-s5/ImageToText-Python-AZURE-AI-OpenSource-App.git
cd ImageToText-Python-AZURE-AI-OpenSource-App
```

### 2️⃣ Create Virtual Environment
```bash
python -m venv venv
source venv/bin/activate
```
Windows:
```powershell
venv\Scripts\activate
```

### 3️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

### 4️⃣ Configure Azure Credentials
```bash
export AZURE_VISION_ENDPOINT="https://<your-resource>.cognitiveservices.azure.com/"
export AZURE_VISION_KEY="<your-api-key>"
```

Windows:
```powershell
setx AZURE_VISION_ENDPOINT "https://<your-resource>.cognitiveservices.azure.com/"
setx AZURE_VISION_KEY "<your-api-key>"
```

### 5️⃣ Run the App
```bash
python src/read-text.py
```

---

## 📊 Output
- Extracted text printed to console

---

## 🚀 Future Enhancements
- Multi-language OCR
- Batch image processing
- PDF to text
- Azure Functions deployment
- Web UI

---

## 👩‍💻 Author
**Ankita Singh**  
Data Scientist | Python | Azure AI | Computer Vision  

🔗 GitHub: https://github.com/ankita-s5  
🔗 LinkedIn: https://www.linkedin.com/in/ankita-singh-50247b3a6/

---

## 📄 License
MIT License

---

> 💡 *Using Azure AI to turn images into actionable data.*
