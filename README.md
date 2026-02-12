 # 📘 AI Study Assistant

A lightweight AI-powered study assistant built using **Flask** and **Ollama (LLaMA 3)**.  
This application allows students to ask academic questions through a clean web interface and receive AI-generated responses.

---

## 🚀 Features

- 🧠 Local AI powered by LLaMA 3 (via Ollama)
- 🌐 Flask web interface
- 💬 Interactive chat UI
- ⚡ Fast response generation
- 🔒 Runs fully offline (when using local Ollama)
- 🌍 Can be deployed for global access

---

## 🏗️ Project Structure

```
.
├── app.py              # Flask backend server
├── ai_agent.py         # AI agent logic (Ollama integration)
├── templates/
│   └── index.html      # Frontend HTML
├── static/
│   ├── style.css       # Styling
│   └── script.js       # Frontend JavaScript
└── README.md
```

---

## 🧠 How It Works

1. User submits a question via web interface.
2. Flask backend receives the request.
3. `ai_agent.py` sends the prompt to Ollama API.
4. LLaMA 3 generates response.
5. Response is returned to frontend and displayed.

---

## 🔧 Requirements

- Python 3.9+
- Flask
- Requests
- Ollama installed locally
- LLaMA 3 model pulled in Ollama

---

## 📦 Installation

### 1️⃣ Clone Repository

```bash
https://github.com/KarthikSharma5025/ai-study-assistant.git
cd ai-study-assistant
```

### 2️⃣ Install Dependencies

```bash
pip install flask requests
```

### 3️⃣ Install Ollama

Download from:

https://ollama.com/

Then pull the model:

```bash
ollama pull llama3
```

---

## ▶️ Running the Application (Local)

```bash
python app.py
```

Open:

```
http://127.0.0.1:5000
```

---

## 🌐 Running for Network Access

Modify `app.py`:

```python
app.run(host="0.0.0.0", port=5000)
```

Then other devices on same WiFi can access:

```
http://YOUR-IP-ADDRESS:5000
```

---

## 🌍 Deploying Globally

To make this accessible worldwide:

- Deploy to a VPS (AWS / DigitalOcean / Render)
- OR use tunneling tools like ngrok
- OR replace Ollama with OpenAI API and deploy to cloud

⚠️ Note: If using Ollama locally, your machine must remain online.

---

## 🔐 Security Recommendations

- Disable `debug=True` in production
- Add authentication system
- Add rate limiting
- Use HTTPS in production
- Never expose local development server publicly without firewall rules

---

## 🎯 Future Improvements

- User login system
- Chat history storage
- Multi-agent support
- File upload support (PDF notes)
- Docker containerization
- Production WSGI server (Gunicorn)

---

## 📜 License

This project is for educational purposes.

---

## 👨‍💻 Author

Built as a custom AI study tool using Flask and local LLM integration.
