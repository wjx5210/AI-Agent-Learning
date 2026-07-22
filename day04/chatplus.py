import os
import json
from pathlib import Path
from dotenv import load_dotenv
from openai import OpenAI


# 加载项目根目录下的 .env
env_path = Path(__file__).parent.parent / ".env"
load_dotenv(dotenv_path=env_path)

api_key = os.getenv("DEEPSEEK_API_KEY")

if not api_key:
    raise ValueError("没有读取到 DEEPSEEK_API_KEY，请检查 .env 文件。")

client = OpenAI(
    api_key=api_key,
    base_url="https://api.deepseek.com"
)

memory_file = Path("messages.json")

if memory_file.exists():
    with open(memory_file, "r", encoding="utf-8") as f:
        messages = json.load(f)
    print("✅ 已加载历史聊天记录")
else:
    messages = [
        {
            "role": "system",
            "content": "你是一个友善、准确的AI助手，请使用中文回答。"
        }
    ]
    print("🆕 创建新的聊天记录")

print("===== AI Chat =====")
print("输入 exit 退出\n")

while True:
    user_input = input("你：").strip()

    if user_input.lower() == "exit":
        print("再见！")
        break

    if not user_input:
        print("请输入内容。\n")
        continue

    messages.append({
        "role": "user",
        "content": user_input
    })

    try:
        response = client.chat.completions.create(
            model="deepseek-chat",
            messages=messages,
            temperature=0.3
        )

        assistant_reply = response.choices[0].message.content

        messages.append({
            "role": "assistant",
            "content": assistant_reply
        })
        with open("messages.json", "w", encoding="utf-8") as f:
            json.dump(messages, f, ensure_ascii=False, indent=4)
        print("\nAI：", assistant_reply)
        print()

    except Exception as error:
        print(f"\n请求失败：{error}\n")