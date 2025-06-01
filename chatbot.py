import os
from dotenv import load_dotenv
import chatgpt

load_dotenv(".env")
chatbot = chatgpt.ChatBot(api_key = os.environ.get("OPENAI_API_KEY"))
system_setting = "じゃんけんをしてください。ユーザーの指定する強さに合わせて、勝率を調整してください。"
chatbot.set_system_setting(system_setting)

print("強さを指定してください '>'")
prompt = input("> ").strip()
message = chatbot.chat(prompt)

print("出す手を教えてください '>'")
prompt = input("> ").strip()
message = chatbot.chat(prompt)
print(message)
