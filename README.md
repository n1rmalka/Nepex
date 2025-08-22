# 📘 Nepex QA Agent

**Nepex QA Agent** is an AI-powered assistant designed to help QA Engineers and Developers generate **test cases, bug reports, release notes, and professional email sign-offs** with ease.  
It uses **OpenAI/LLM APIs** in the backend with a **Flask + Jinja2 frontend** for a simple, user-friendly interface.  

---

## 🚀 Features
- 🧪 **Test Case Generation** – Create structured test cases from user stories.  
- 🐞 **Bug Report Drafting** – Generate clear and reproducible bug reports.  
- 📝 **Release Notes Creation** – Summarize software updates into end-user friendly notes.  
- 📧 **Email Signoffs** – Write polished and professional QA sign-offs.  
- 💾 **Export to TXT** – Save results in a `.txt` file.  
- 📋 **Copy Output** – Quick copy to clipboard functionality.  

---

## 🛠️ Tech Stack
- **Backend**: Python, Flask  
- **Frontend**: HTML, CSS (Jinja2 templates)  
- **AI Model**: OpenAI API / OpenRouter API  
- **Other Tools**: dotenv for API key management  

---

## 📂 Project Structure
```
nepex/
├── app/
│   ├── main.py              # Flask backend
│   ├── nepex_agent.py       # Core AI logic
├── templates/
│   └── index.html           # Web UI
├── static/
│   ├── style.css            # Styling
│   └── script.js            # Copy & UI interactions
├── .env                     # API keys (not committed to git)
├── requirements.txt         # Python dependencies
└── README.md                # Project documentation
```

---

## ⚙️ Setup & Installation

1. **Clone the repo**
   ```bash
   git clone https://github.com/yourusername/nepex.git
   cd nepex
   ```

2. **Create virtual environment & activate**
   ```bash
   python -m venv venv
   source venv/bin/activate   # Mac/Linux
   venv\Scripts\activate      # Windows
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure API Key**
   - Create a `.env` file in the project root:
     ```
     OPENAI_API_KEY=your_api_key_here
     ```
     or if using OpenRouter:
     ```
     OPENROUTER_API_KEY=your_openrouter_key_here
     ```

---

## ▶️ Run the Application

```bash
python app/main.py
```

- App will start at **http://127.0.0.1:5000/**
- Open in browser to access the Nepex QA Agent UI.

---

## 🧑‍💻 Usage
1. Select a **Use Case** (Test Case, Bug Report, Release Notes, Email Signoff).  
2. Paste or type your **prompt input** (e.g., user story, bug description, feature change).  
3. Click **Get Result**.  
4. Copy output or **Export as .txt** file.  

---

## 📌 Example
**Input (Use Case: Test Case)**  
> User story: As a user, I want to reset my password via email so that I can regain access to my account.  

**Output**  
- Test cases for password reset, invalid email, expired link, successful login, etc.  

---

## 🤝 Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you’d like to improve.  

---

## 📜 License
This project is licensed under the **MIT License** – feel free to use and adapt.  

---

## 📬 Connect with Me  

- 💼 [LinkedIn – Nirmal Patel](https://www.linkedin.com/in/nirmalka-patel/)  
- ✍️ [Medium – Nirmal Kiran Patel](https://medium.com/@n1rmalka)  
