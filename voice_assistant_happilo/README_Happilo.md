# 🎙️ Happilo — AI Voice Assistant v5.0

A Python-based personal AI voice assistant that listens to your voice commands and responds intelligently. Wake it up anytime by saying **"Hey Happilo"**!

---

## ✨ Features

| Command | What it does |
|---------|-------------|
| ⏰ "What time is it?" | Tells current time |
| 📅 "What is today's date?" | Tells current date |
| 🌤 "Weather in Mumbai" | Fetches live weather |
| 🔍 "Search latest AI news" | Web search |
| ▶ "Open YouTube" / "Play lo-fi music" | Opens YouTube / plays music |
| 🤖 "Open ChatGPT" | Opens ChatGPT in browser |
| 🌐 "Open Google" / "Open Amazon" / "Open Flipkart" | Opens websites |
| 📰 "Read the news" | Reads latest news headlines |
| 📖 "Who is Elon Musk?" | Wikipedia search |
| 💻 "Open Notepad" / "Open Calculator" | Opens desktop apps |
| 🔋 "What is my battery?" | Checks battery percentage |
| 🔒 "Lock my screen" | Locks the PC |
| 💻 "Shutdown" / "Restart" | Shuts down or restarts PC |
| 📖 "Meaning of eloquent" | Dictionary lookup |
| 💱 "Convert 100 USD to INR" | Currency conversion |
| 👋 "Goodbye" | Exits the assistant |

---

## 🗂️ Project Structure

```
voice_assistant_happilo/
├── main.py           # Entry point — runs the assistant
├── assistant.py      # Core assistant logic (listen, speak, wake word)
├── commands.py       # All command handlers
├── requirements.txt # Dependencies
├──API_KEYS_GUIDE.md    
└── README.md
```

---

## ⚙️ Setup & Installation

### 1. Clone the repo
```bash
git clone https://github.com/AnushreeRPoojary/voice_assistant_happilo.git
cd voice_assistant_happilo
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Run the assistant
```bash
python main.py
```

---

## 📦 Requirements

```
speechrecognition
pyttsx3
pyaudio
wikipedia
requests
psutil
```

> **Note:** On Windows, if `pyaudio` install fails, use:
> ```bash
> pip install pipwin
> pipwin install pyaudio
> ```

---

## 🚀 How to Use

1. Run `python main.py`
2. Wait for the greeting message
3. Say **"Hey Happilo"** to wake it up
4. Speak your command clearly
5. Say **"Goodbye"** to exit

---

## 🛠️ Tech Stack

- Python 3
- SpeechRecognition — voice input
- pyttsx3 — text to speech
- PyAudio — microphone access
- Wikipedia API — knowledge queries
- webbrowser — open websites
- psutil — battery & system info
- requests — weather & news APIs

---

## 👩‍💻 Author

**Anushree R Poojary**  
[GitHub](https://github.com/AnushreeRPoojary)
*Built by Anushree R — AI & ML Engineer*  
*B.E. Artificial Intelligence & Machine Learning, SMVITM Udupi*
