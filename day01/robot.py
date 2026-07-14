#命令行聊天机器人
print("欢迎来到AI Agent聊天机器人！")
while True:
    text = input("你:")
    if text == "退出":
        print("机器人:再见！")
        break
    print("机器人:你说的是:", text)