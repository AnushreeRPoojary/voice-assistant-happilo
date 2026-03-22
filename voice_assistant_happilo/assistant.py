# ============================================================
# HAPPILO — AI Voice Assistant v5.0
# Author : Anushree R
# Email  : anushreerpoojary2611@gmail.com
# GitHub : github.com/AnushreeRPoojary
# ============================================================

import speech_recognition as sr
import pyttsx3
import datetime


class VoiceAssistant:
    def __init__(self, name="Happilo"):
        self.name = name
        self.wake_word = "hey happilo"
        self.wake_word_variants = [
            "hey happilo", "hi happilo", "ok happilo", "okay happilo",
            "happilo", "hey hapilo", "hey hapillo", "hey appilo",
            "hey hepilo", "hey happila", "hey happilu",
            "hey happy lo", "happy lo", "stay happilo",
            "happy love", "h e y h a p p i l o",
        ]
        self.recognizer = sr.Recognizer()
        self.engine = pyttsx3.init()
        self.memory = []
        self._configure_voice()

    def _configure_voice(self):
        voices = self.engine.getProperty("voices")
        try:
            self.engine.setProperty("voice", voices[1].id)
        except IndexError:
            self.engine.setProperty("voice", voices[0].id)
        self.engine.setProperty("rate", 170)
        self.engine.setProperty("volume", 1.0)

    def speak(self, text: str):
        print(f"\n[Happilo]: {text}")
        self.engine.say(text)
        self.engine.runAndWait()

    def remember(self, role: str, text: str):
        self.memory.append({"role": role, "text": text})
        if len(self.memory) > 10:
            self.memory.pop(0)

    def get_last_user_said(self) -> str:
        for item in reversed(self.memory):
            if item["role"] == "user":
                return item["text"]
        return ""

    def listen(self, timeout: int = 6) -> str | None:
        with sr.Microphone() as source:
            print("\n🎤 [Listening... speak now]")
            self.recognizer.adjust_for_ambient_noise(source, duration=0.6)
            try:
                audio = self.recognizer.listen(source, timeout=timeout, phrase_time_limit=12)
                query = self.recognizer.recognize_google(audio).lower()
                print(f"[You]: {query}")
                self.remember("user", query)
                return query
            except sr.WaitTimeoutError:
                print("[Timeout] No speech detected.")
            except sr.UnknownValueError:
                print("[Error] Could not understand. Please speak clearly.")
            except sr.RequestError as e:
                print(f"[Network Error] Speech service unavailable: {e}")
            except Exception as e:
                print(f"[Error] {e}")
        return None

    def listen_for_wake_word(self) -> bool:
        with sr.Microphone() as source:
            print("\n😴 [Waiting for wake word: 'Hey Happilo'...]")
            self.recognizer.adjust_for_ambient_noise(source, duration=0.3)
            try:
                audio = self.recognizer.listen(source, timeout=8, phrase_time_limit=5)
            except sr.WaitTimeoutError:
                return False
            except Exception as e:
                print(f"[Mic Error] {e}")
                return False

            try:
                text = self.recognizer.recognize_google(audio).lower().strip()
                print(f"[Heard]: {text}")

                for variant in self.wake_word_variants:
                    if variant in text:
                        print(f"[Wake word matched]: '{variant}'")
                        return True

                happilo_sounds = ["happilo", "hapilo", "hapillo", "appilo", "hepilo", "happila"]
                for sound in happilo_sounds:
                    if sound in text:
                        print(f"[Wake word fuzzy matched]: '{text}'")
                        return True

                no_spaces = text.replace(" ", "")
                if "happilo" in no_spaces:
                    print(f"[Wake word spelled matched]: '{text}'")
                    return True

            except sr.UnknownValueError:
                pass
            except sr.RequestError as e:
                print(f"[Network Error] Speech service unavailable: {e}")
            except Exception as e:
                print(f"[Error] {e}")

        return False

    def greet(self):
        hour = datetime.datetime.now().hour
        if 5 <= hour < 12:
            greeting = "Good morning"
        elif 12 <= hour < 17:
            greeting = "Good afternoon"
        else:
            greeting = "Good evening"
        self.speak(
            f"{greeting}! I am Happilo, your personal AI voice assistant. "
            "Say Hey Happilo to wake me up anytime!"
        )
