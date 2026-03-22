# ============================================================
# HAPPILO — AI Voice Assistant v5.0
# Author : Anushree R
# Email  : anushreerpoojary2611@gmail.com
# GitHub : github.com/AnushreeRPoojary
# ============================================================

import datetime
import webbrowser
import os
import sys
import requests


def get_time() -> str:
    now = datetime.datetime.now()
    return f"The current time is {now.strftime('%I:%M %p')}."


def get_date() -> str:
    today = datetime.date.today()
    return f"Today is {today.strftime('%A, %B %d, %Y')}."


def get_weather(city: str, api_key: str = "") -> str:
    if not api_key or api_key == "YOUR_WEATHER_API_KEY":
        webbrowser.open(f"https://www.google.com/search?q=weather+in+{city.replace(' ', '+')}")
        return f"Opening Google weather for {city}. Add your OpenWeatherMap API key in main.py for spoken weather."
    try:
        url = "https://api.openweathermap.org/data/2.5/weather"
        params = {"q": city, "appid": api_key, "units": "metric"}
        res = requests.get(url, params=params, timeout=5)
        data = res.json()
        if data.get("cod") != 200:
            return f"Could not find weather for {city}."
        temp  = data["main"]["temp"]
        feels = data["main"]["feels_like"]
        desc  = data["weather"][0]["description"].capitalize()
        humid = data["main"]["humidity"]
        return (f"Weather in {city.title()}: {desc}. "
                f"Temperature {temp}°C, feels like {feels}°C. "
                f"Humidity {humid} percent.")
    except Exception:
        return "Could not fetch weather. Check your internet connection."


def search_google(query: str) -> str:
    webbrowser.open(f"https://www.google.com/search?q={query.replace(' ', '+')}")
    return f"Searching Google for: {query}"


def open_youtube(query: str = "") -> str:
    if query:
        webbrowser.open(f"https://www.youtube.com/results?search_query={query.replace(' ', '+')}")
        return f"Searching YouTube for: {query}"
    webbrowser.open("https://www.youtube.com")
    return "Opening YouTube."


def open_chatgpt() -> str:
    webbrowser.open("https://chat.openai.com")
    return "Opening ChatGPT."


def open_google() -> str:
    webbrowser.open("https://www.google.com")
    return "Opening Google."


def open_website_by_name(name: str) -> str:
    sites = {
        "amazon"       : "https://www.amazon.in",
        "flipkart"     : "https://www.flipkart.com",
        "instagram"    : "https://www.instagram.com",
        "twitter"      : "https://www.twitter.com",
        "facebook"     : "https://www.facebook.com",
        "whatsapp"     : "https://web.whatsapp.com",
        "linkedin"     : "https://www.linkedin.com",
        "spotify"      : "https://open.spotify.com",
        "reddit"       : "https://www.reddit.com",
        "stackoverflow": "https://stackoverflow.com",
        "chatgpt"      : "https://chat.openai.com",
        "github"       : "https://www.github.com",
        "gmail"        : "https://mail.google.com",
        "netflix"      : "https://www.netflix.com",
        "google"       : "https://www.google.com",
        "youtube"      : "https://www.youtube.com",
        "hotstar"      : "https://www.hotstar.com",
        "swiggy"       : "https://www.swiggy.com",
        "zomato"       : "https://www.zomato.com",
    }
    key = name.lower().strip()
    url = sites.get(key)
    if url:
        webbrowser.open(url)
        return f"Opening {name.title()}."
    webbrowser.open(f"https://www.{key}.com")
    return f"Trying to open {name}."


def search_wikipedia(query: str) -> str:
    try:
        import wikipedia
        return wikipedia.summary(query, sentences=2)
    except ImportError:
        return "Wikipedia module not installed. Run: pip install wikipedia"
    except Exception:
        return f"Could not find Wikipedia info for: {query}"


def get_news(api_key: str = "") -> str:
    if not api_key or api_key == "YOUR_NEWS_API_KEY":
        webbrowser.open("https://news.google.com")
        return "Opening Google News. Add your NewsAPI key in main.py for spoken headlines."
    try:
        url = "https://newsapi.org/v2/top-headlines"
        params = {"country": "in", "pageSize": 5, "apiKey": api_key}
        res = requests.get(url, params=params, timeout=5)
        data = res.json()
        articles = data.get("articles", [])
        if not articles:
            return "No news found right now."
        headlines = [f"{i+1}. {a['title']}" for i, a in enumerate(articles[:5])]
        return "Top 5 headlines: " + ". ".join(headlines)
    except Exception:
        return "Could not fetch news. Check your internet connection."


def open_application(app_name: str) -> str:
    windows_apps = {
        "notepad"   : "notepad.exe",
        "calculator": "calc.exe",
        "paint"     : "mspaint.exe",
        "explorer"  : "explorer.exe",
    }
    mac_apps = {
        "notes"     : "Notes",
        "calculator": "Calculator",
        "terminal"  : "Terminal",
        "finder"    : "Finder",
    }
    name = app_name.lower().strip()
    if sys.platform == "win32":
        exe = windows_apps.get(name)
        if exe:
            os.system(f"start {exe}")
            return f"Opening {app_name}."
    elif sys.platform == "darwin":
        app = mac_apps.get(name)
        if app:
            os.system(f"open -a '{app}'")
            return f"Opening {app_name}."
    return open_website_by_name(app_name)


def open_github() -> str:
    webbrowser.open("https://github.com/AnushreeRPoojary")
    return "Opening your GitHub."


def open_gmail() -> str:
    webbrowser.open("https://mail.google.com")
    return "Opening Gmail."


def open_netflix() -> str:
    webbrowser.open("https://www.netflix.com")
    return "Opening Netflix."


def get_battery() -> str:
    try:
        import psutil
        battery = psutil.sensors_battery()
        if battery is None:
            return "No battery detected. You may be on a desktop PC."
        percent = battery.percent
        plugged = "plugged in" if battery.power_plugged else "not plugged in"
        return f"Battery is at {int(percent)} percent and is {plugged}."
    except ImportError:
        return "psutil not installed. Run: pip install psutil"
    except Exception as e:
        return f"Could not get battery info: {e}"


def shutdown_pc() -> str:
    if sys.platform == "win32":
        os.system("shutdown /s /t 5")
        return "Shutting down your PC in 5 seconds."
    elif sys.platform == "darwin":
        os.system("sudo shutdown -h now")
        return "Shutting down your Mac."
    else:
        os.system("sudo shutdown now")
        return "Shutting down."


def restart_pc() -> str:
    if sys.platform == "win32":
        os.system("shutdown /r /t 5")
        return "Restarting your PC in 5 seconds."
    elif sys.platform == "darwin":
        os.system("sudo shutdown -r now")
        return "Restarting your Mac."
    else:
        os.system("sudo reboot")
        return "Restarting."


def lock_screen() -> str:
    if sys.platform == "win32":
        os.system("rundll32.exe user32.dll,LockWorkStation")
        return "Locking your screen."
    elif sys.platform == "darwin":
        os.system("pmset displaysleepnow")
        return "Locking your screen."
    else:
        os.system("xdg-screensaver lock")
        return "Locking your screen."


def get_meaning(word: str) -> str:
    try:
        url = f"https://api.dictionaryapi.dev/api/v2/entries/en/{word.strip()}"
        res = requests.get(url, timeout=5)
        data = res.json()
        if isinstance(data, list) and data:
            meanings = data[0].get("meanings", [])
            if meanings:
                part    = meanings[0].get("partOfSpeech", "")
                defs    = meanings[0].get("definitions", [])
                meaning = defs[0].get("definition", "") if defs else ""
                return f"{word.title()} is a {part}. It means: {meaning}"
        return f"Could not find meaning for: {word}"
    except Exception:
        return "Could not fetch dictionary. Check your internet connection."


def convert_currency(amount: float, from_cur: str, to_cur: str) -> str:
    try:
        url = f"https://api.exchangerate-api.com/v4/latest/{from_cur.upper()}"
        res = requests.get(url, timeout=5)
        data = res.json()
        rates = data.get("rates", {})
        rate  = rates.get(to_cur.upper())
        if not rate:
            return f"Could not find exchange rate for {to_cur}."
        result = round(amount * rate, 2)
        return f"{amount} {from_cur.upper()} equals {result} {to_cur.upper()}."
    except Exception:
        return "Could not fetch exchange rates. Check your internet connection."
