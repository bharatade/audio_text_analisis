#from openai import OpenAI
from groq import Groq
from configs.config import LLM_MODEL


GROQ_API_KEY = "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"

#client = OpenAI(base_url="xxxxx", api_key="ollama")
client = Groq(api_key=GROQ_API_KEY)

def translate_to_english(text):
    chat = client.chat.completions.create(
        model=LLM_MODEL,
        messages=[{"role": "user", "content": f"Translate to English:\n\n{text}"}],
        temperature=0.0
    )
    return chat.choices[0].message.content.strip()

def classify_busy(text):
    prompt = f"""Decide if the speaker is BUSY. Transcript:\n\"\"\"{text}\"\"\""""
    chat = client.chat.completions.create(
        model=LLM_MODEL,
        messages=[{"role": "user", "content": prompt}],
        temperature=0.0
    )
    return 1 if "true" in chat.choices[0].message.content.lower() else 0

def generate_summary(text):
    if not text.strip():
        return "No conversation detected."
    chat = client.chat.completions.create(
        model=LLM_MODEL,
        messages=[{"role": "user", "content": f"Summarize this:\n\n{text}"}],
        temperature=0.3
    )
    return chat.choices[0].message.content.strip()
