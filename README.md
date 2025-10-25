# 🤖 AI-Friendly Chatbot — “Neura”

A **friendly AI chatbot** that blends **rule-based logic** with **GPT-powered intelligence** for meaningful, context-aware conversations.  
This console-based chatbot securely uses **API key authentication** and maintains chat history locally for a personalized experience.

---

## 🧩 Features

- 💬 **Hybrid Chat Logic** — Combines GPT API with rule-based responses for efficiency and natural flow.  
- 🔐 **Secure API Key Integration** — Uses environment variables for key protection.  
- 🧠 **Contextual Memory** — Retains previous chats for continuity.  
- 😄 **Mood Emojis** — Dynamically adds emojis to reflect tone and personality.  
- 🗂️ **Chat History Logging** — Automatically saves conversations in `data/chat_history.txt`.  
- ⚡ **Lightweight & Fast** — Command-line interface with minimal dependencies.

---

## 🏗️ Project Structure

```
AI-Friendly-Chatbot/
│
├── chatbot_logic/
│   ├── gpt_integration.py      
│   ├── rules.py                
│   ├── utils.py                
│
├── data/
│   └── chat_history.txt        
│
├── .env                        
├── .gitignore                  
├── requirements.txt            
├── main.py                     
└── README.md                   
```

---

## ⚙️ Setup Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/Mamoonkhan11/AI-Friendly-Chatbot.git
cd AI-Friendly-Chatbot
```

### 2. Create a Virtual Environment
```bash
python -m venv venv
source venv/bin/activate      # Linux/Mac
venv\Scripts\activate         # Windows
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables
Create a `.env` file in the project root:
```
OPENAI_API_KEY=your_openai_api_key_here
```

### 5. Run the Chatbot
```bash
python main.py
```

---

## 🧠 How It Works

1. **Startup** – Loads the OpenAI API key from `.env` and reads previous chat logs.  
2. **Conversation** – Takes user input and first checks for **rule-based replies**.  
3. **AI Response** – If no rule matches, the chatbot sends the message to **GPT API**.  
4. **Memory** – Logs the full conversation in `data/chat_history.txt` for continuity.  
5. **User Experience** – Adds emotional touch with smart **emoji selection**.

---

## 💬 Example Interaction

```
Welcome to Friendly AI Chatbot!
What's your name? Mamoon

Hello Mamoon! I'm Neura, your friendly AI assistant. 🌸
Type 'quit' to exit.

Mamoon: Hi there!
Neura: Hello Mamoon! How are you feeling today? 😊

Mamoon: Tell me a fun fact
Neura: Did you know honey never spoils? 🍯
```

---

## 🧰 Dependencies

- **Python 3.8+**
- **dotenv** – For secure API key loading  
- **openai** – For GPT model integration  

Install all dependencies via:
```bash
pip install -r requirements.txt
```

---

## 🔒 Security Notes

- Never hardcode your API key — always store it in `.env`.  
- Add `.env` and `data/chat_history.txt` to your `.gitignore`.  
- Avoid committing any private logs or credentials.

---

## 📈 Future Enhancements

- 🌐 Web-based UI using Streamlit or Flask  
- 💾 Database integration for scalable chat history  
- 🗣️ Voice input/output support  
- 🎨 Custom themes for chat experience  

---

## 🧑‍💻 Author

**Mamoon Khan**  
[GitHub Profile](https://github.com/Mamoonkhan11)  
Friendly AI — built with ❤️ and Python.
