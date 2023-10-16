import os
from dotenv import load_dotenv
import openai

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")

prompt = open("prompt.md", "r").read()

print("[Q] " + prompt)

response = openai.ChatCompletion.create(
    # model="gpt-4",
    model="gpt-4-0314",
    messages=[
        {
            "role": "user",
            "content": prompt
        }
    ]
)

msg = response.choices[0].message['content']

with open("output.txt", "w") as f:
    f.write(msg)

print("[A] " + msg)
