
## 👩‍💻 Author

| | |
|---|---|
| **Name** | Anushree R |
| **Email** | anushreerpoojary2611@gmail.com |
| **GitHub** | [github.com/AnushreeRPoojary](https://github.com/AnushreeRPoojary) |

---
# How to Get Free API Keys for happilo or u can name it as cyra too anything u want

---

## 1. Weather API Key (OpenWeatherMap) — FREE

1. Go to https://openweathermap.org/api
2. Click "Sign Up" — it's free
3. Enter your name, email, password
4. Verify your email
5. Go to https://home.openweathermap.org/api_keys
6. Copy the API key shown there
7. Open `main.py` in Notepad or your code editor
8. Replace this line:
   ```
   WEATHER_API_KEY = "YOUR_WEATHER_API_KEY"
   ```
   with your key like:
   ```
   WEATHER_API_KEY = "abc123yourkeyhere"
   ```
9. Save the file

> ⚠️ **Important:** New OpenWeatherMap keys take **up to 2 hours** to activate.
> If you get an error right after signing up, just wait and try again later.

Now happilo will speak the weather for any city!

---

## 2. News API Key (NewsAPI) — FREE

1. Go to https://newsapi.org
2. Click "Get API Key" — it's free
3. Enter your name, email, password
4. Verify your email
5. Copy the API key from your dashboard
6. Open `main.py` in Notepad or your code editor
7. Replace this line:
   ```
   NEWS_API_KEY = "YOUR_NEWS_API_KEY"
   ```
   with your key like:
   ```
   NEWS_API_KEY = "xyz789yourkeyhere"
   ```
8. Save the file

> ⚠️ **Note:** The free NewsAPI plan only works on localhost (your own PC).
> It does **not** work if you deploy happilo to a server — upgrade to paid for that.

Now happilo will read the top 5 Indian news headlines!

---

## Without API Keys

| Feature   | Without Key                        | With Key                    |
|-----------|------------------------------------|-----------------------------|
| 🌤 Weather | Opens Google weather in browser    | happilo speaks the weather     |
| 📰 News    | Opens Google News in browser       | happilo reads top 5 headlines  |

Everything else works without any API key — no sign-up needed.

---

## Troubleshooting

**Weather says "Invalid API key"?**
→ Wait 1–2 hours after signing up. OpenWeatherMap keys are not instant.

**News returns no articles?**
→ Make sure you copied the full key with no spaces. Check your NewsAPI dashboard.

**Still not working?**
→ Double-check that you saved `main.py` after pasting the key.
→ Make sure there are no extra quotes or spaces inside the string.
