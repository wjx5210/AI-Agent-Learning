import os
from pathlib import Path

from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI


# 加载环境变量
env_path = Path(__file__).parent.parent / ".env"
load_dotenv(env_path)

api_key = os.getenv("DEEPSEEK_API_KEY")

model = ChatOpenAI(
    model="deepseek-chat",
    api_key=api_key,
    base_url="https://api.deepseek.com",
    temperature=0.3
)

prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "你是一位专业Python老师，请使用中文回答。"
        ),
        (
            "human",
            "{question}"
        )
    ]
)
#创建一个链，将 prompt 和 model 连接起来
chain = prompt | model

response = chain.invoke(
    {
        "question": "Python是什么？"
    }
)

print(response.content)