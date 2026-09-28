import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

api_key = os.getenv("GROQ_API_KEY")

if not api_key:
    raise ValueError("GROQ_API_KEY was not found in .env")

client = Groq(api_key=api_key)

response = client.chat.completions.create(
    model="openai/gpt-oss-20b",
    messages=[
        {
            "role": "user",
            "content": "Explain in one sentence what a hardware failure is."
        }
    ],
)

print("\n========== GROQ AI RESPONSE ==========")
print(response.choices[0].message.content)
print("\n========== TEST SUCCESSFUL ==========")