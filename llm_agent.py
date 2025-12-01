# llm_agent.py
import os
from dotenv import load_dotenv
import ollama

load_dotenv()
MODEL = os.getenv("OLLAMA_MODEL", "llama3.1")

def generate_linkedin_post(user_prompt: str, tone: str = "professional"):
    """
    Creates a LinkedIn-ready post for ANY input prompt.
    Not limited to certifications anymore.
    """

    prompt = f"""
You are an expert LinkedIn content writer.

Your job is to take a user's prompt and turn it into a polished, engaging,
LinkedIn-ready post.

User prompt:
\"\"\"{user_prompt}\"\"\"

Requirements:
- Write naturally like a human (not robotic).
- Keep it concise yet impactful.
- Use short paragraphs (2–5 lines each).
- Add relevant insights, meaning, or takeaway.
- Optional emojis allowed but not necessary.
- End with 2–5 relevant hashtags.
- Tone: {tone}

Return ONLY the final LinkedIn post.
"""

    res = ollama.chat(model=MODEL, messages=[
        {"role": "user", "content": prompt}
    ])

    return res["message"]["content"].strip()
