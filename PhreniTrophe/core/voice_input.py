import speech_recognition as sr

def listen_meal():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("🎙 Speak your meal...")
        audio = r.listen(source)
    try:
        text = r.recognize_google(audio)
        print(f"🗣 You said: {text}")
        return text.lower()
    except Exception as e:
        print(f"⚠️ Voice error: {e}")
        return None
