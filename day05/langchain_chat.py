import os
from pathlib import Path

from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.messages import SystemMessage, HumanMessage


# 加载项目根目录下的 .env
env_path = Path(__file__).parent.parent / ".env"
load_dotenv(dotenv_path=env_path)

api_key = os.getenv("DEEPSEEK_API_KEY")

if not api_key:
    raise ValueError("没有读取到 DEEPSEEK_API_KEY，请检查 .env 文件。")


# 创建 LangChain 模型
model = ChatOpenAI(
    model="deepseek-chat",
    api_key=api_key,
    base_url="https://api.deepseek.com",
    temperature=0.3
)


# 初始化聊天记录
messages = [
    SystemMessage(
        content="你是一位专业的Python学习教练，请使用中文回答。"
    )
]


print("===== LangChain Chat =====")
print("输入 exit 退出\n")


while True:
    user_input = input("你：").strip()

    if user_input.lower() == "exit":
        print("再见！")
        break

    if not user_input:
        print("请输入内容。\n")
        continue

    # 将用户输入封装成 HumanMessage
    messages.append(
        HumanMessage(content=user_input)
    )

    try:
        # 发送完整聊天历史
        response = model.invoke(messages)

        # response 已经是 AIMessage，可以直接加入历史记录
        messages.append(response)

        print("\nAI：", response.content)
        print()

    except Exception as error:
        print(f"\n请求失败：{error}\n")