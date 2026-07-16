import os
from pathlib import Path
from dotenv import load_dotenv
from openai import OpenAI

# 加载 .env
env_path = Path(__file__).parent.parent / ".env"
load_dotenv(dotenv_path=env_path)

client = OpenAI(
    api_key=os.getenv("DEEPSEEK_API_KEY"),
    base_url="https://api.deepseek.com"
)

print("===== AI Chat =====")
print("输入 exit 退出\n")

while True:
    user_input = input("你：")

    if user_input.lower() == "exit":
        print("再见！")
        break

    response = client.chat.completions.create(
        model="deepseek-chat",
        messages=[
            {
                "role": "user",
                "content": user_input
            }
        ]
    )

    print("\nAI：")
    print(response.choices[0].message.content)
    print()