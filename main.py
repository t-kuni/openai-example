import os
from dotenv import load_dotenv
import openai
import pygame
import time


def play_completion_sound():
    # pygameを初期化
    pygame.mixer.init()

    # 音声ファイルを読み込む (この例では'complete.wav'という名前の音声ファイルを使用)
    pygame.mixer.music.load('complete.wav')

    # 音声を再生
    pygame.mixer.music.play()

    # 音声が終わるまで待つ
    while pygame.mixer.music.get_busy():
        time.sleep(0.1)


load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")

prompt = open("prompt.md", "r").read()

# print("[Q] " + prompt)

response = openai.ChatCompletion.create(
    # model="gpt-4",
    model="gpt-4-1106-preview",
    messages=[
        {
            "role": "user",
            "content": prompt
        }
    ]
)

msg = response.choices[0].message['content']

with open("output.md", "w") as f:
    f.write(msg)

# print("[A] " + msg)

play_completion_sound()
