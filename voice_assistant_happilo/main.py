# ============================================================
# HAPPILO — AI Voice Assistant v5.0
# Author : Anushree R
# Email  : anushreerpoojary2611@gmail.com
# GitHub : github.com/AnushreeRPoojary
# ============================================================

from assistant import VoiceAssistant
from commands import (
    get_time, get_date, get_weather,
    search_google, open_youtube, open_chatgpt, open_google,
    search_wikipedia, get_news,
    open_application, open_github, open_gmail, open_netflix,
    get_battery,
    shutdown_pc, restart_pc, lock_screen,
    get_meaning,
    convert_currency,
)
import re

WEATHER_API_KEY = "YOUR_WEATHER_API_KEY"
NEWS_API_KEY    = "YOUR_NEWS_API_KEY"

USE_WAKE_WORD = False


def process_command(query: str, assistant: VoiceAssistant) -> bool:

    if any(w in query for w in ["exit", "quit", "bye", "goodbye", "stop"]):
        assistant.speak("Goodbye! Have a wonderful day.")
        return False

    elif "time" in query:
        assistant.speak(get_time())

    elif "date" in query or "today" in query:
        assistant.speak(get_date())

    elif "weather" in query:
        city = (query.replace("weather", "").replace("in", "")
                     .replace("what is the", "").replace("what's the", "").strip()) or "your city"
        assistant.speak(get_weather(city, WEATHER_API_KEY))

    elif "chatgpt" in query:
        assistant.speak(open_chatgpt())

    elif "open google" in query:
        assistant.speak(open_google())

    elif "news" in query or "headlines" in query:
        assistant.speak(get_news(NEWS_API_KEY))

    elif "meaning of" in query or "define" in query or "what does" in query:
        word = (query.replace("meaning of", "").replace("define", "")
                     .replace("what does", "").replace("mean", "").strip())
        assistant.speak(get_meaning(word) if word else "Which word would you like me to define?")

    elif "convert" in query or ("to" in query and any(c in query for c in ["usd", "inr", "eur", "gbp", "jpy"])):
        numbers    = re.findall(r'\d+\.?\d*', query)
        amount     = float(numbers[0]) if numbers else 1.0
        currencies = re.findall(r'\b(usd|inr|eur|gbp|jpy|aed|cad|aud)\b', query)
        if len(currencies) >= 2:
            assistant.speak(convert_currency(amount, currencies[0], currencies[1]))
        else:
            assistant.speak("Please say something like: convert 100 USD to INR.")

    elif "lock" in query and ("screen" in query or "pc" in query or "computer" in query):
        assistant.speak(lock_screen())

    elif "battery" in query:
        assistant.speak(get_battery())

    elif "shutdown" in query or "shut down" in query:
        assistant.speak("Are you sure? Say yes to confirm shutdown.")
        confirm = assistant.listen()
        if confirm and "yes" in confirm:
            assistant.speak(shutdown_pc())
        else:
            assistant.speak("Shutdown cancelled.")

    elif "restart" in query or "reboot" in query:
        assistant.speak("Are you sure? Say yes to confirm restart.")
        confirm = assistant.listen()
        if confirm and "yes" in confirm:
            assistant.speak(restart_pc())
        else:
            assistant.speak("Restart cancelled.")

    elif any(w in query for w in ["who is", "wikipedia", "tell me about"]):
        term = (query.replace("who is", "").replace("wikipedia", "")
                     .replace("tell me about", "").strip())
        if term:
            assistant.speak(f"Let me look up {term}.")
            assistant.speak(search_wikipedia(term))
        else:
            assistant.speak("What would you like me to look up?")

    elif "youtube" in query or "play" in query:
        term = query.replace("youtube", "").replace("play", "").replace("search", "").strip()
        assistant.speak(open_youtube(term))

    elif "github" in query:
        assistant.speak(open_github())

    elif "gmail" in query or "email" in query:
        assistant.speak(open_gmail())

    elif "netflix" in query:
        assistant.speak(open_netflix())

    elif "search" in query or "google" in query:
        term = query.replace("search", "").replace("google", "").strip()
        assistant.speak(search_google(term) if term else "What would you like to search?")

    elif "open" in query:
        site_or_app = query.replace("open", "").strip()
        assistant.speak(open_application(site_or_app))

    elif "your name" in query or "who are you" in query:
        assistant.speak("I am Happilo, your personal AI voice assistant built entirely in Python.")

    elif "help" in query or "what can you do" in query:
        assistant.speak(
            "I can check time and date, weather, search Google, open YouTube, "
            "open ChatGPT, read news, search Wikipedia, open any website or app, "
            "check battery, lock screen, shutdown or restart PC, "
            "define words, and convert currency."
        )

    else:
        assistant.speak("I did not catch that. Say help to hear what I can do.")

    return True


def print_banner():
    print("""
╔══════════════════════════════════════════════════════════╗
║         HAPPILO — AI Voice Assistant  v5.0               ║
╠══════════════════════════════════════════════════════════╣
║  ⏰  "What time is it?"                                  ║
║  📅  "What is today's date?"                             ║
║  🌤  "Weather in Mumbai"                                 ║
║  🔍  "Search latest AI news"                             ║
║  ▶   "Open YouTube" / "Play lo-fi music"                 ║
║  🤖  "Open ChatGPT"                                      ║
║  🌐  "Open Google" / "Open Amazon" / "Open Flipkart"     ║
║  📰  "Read the news"                                     ║
║  📖  "Who is Elon Musk?"  (Wikipedia)                    ║
║  💻  "Open Notepad" / "Open Calculator"                  ║
║  🔋  "What is my battery?"                               ║
║  🔒  "Lock my screen"                                    ║
║  💻  "Shutdown" / "Restart"                              ║
║  📖  "Meaning of eloquent"                               ║
║  💱  "Convert 100 USD to INR"                            ║
║  👋  "Goodbye" to quit                                   ║
╚══════════════════════════════════════════════════════════╝
    """)


def main():
    assistant = VoiceAssistant(name="Happilo")
    print_banner()
    assistant.greet()

    while True:
        try:
            if USE_WAKE_WORD:
                detected = assistant.listen_for_wake_word()
                if not detected:
                    continue
                assistant.speak("Yes, I am listening.")

            query = assistant.listen()
            if query is None:
                continue
            if not process_command(query, assistant):
                break

        except KeyboardInterrupt:
            assistant.speak("Shutting down. Goodbye!")
            break


if __name__ == "__main__":
    main()
