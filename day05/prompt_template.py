from langchain_core.prompts import ChatPromptTemplate

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

messages = prompt.invoke(
    {
        "question": "Python是什么？"
    }
)

print(messages)