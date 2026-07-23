# AI-Agent-Learning
记录我的AI Agent学习过程
## 学习计划
- [1] Day 1 Python基础 Git GitHub
- [2] Day 2 面向对象 虚拟环境 pip
- [3] Day 3 调用第一个大模型API 制作命令行聊天机器人
今天我遇到了两个网络问题：
1. DeepSeek API SSL 报错
    * 原因：Windows 用户代理 (127.0.0.1:26561) 残留，导致 Python HTTPS 请求证书验证失败。
2. GitHub git push 连接重置
    * 原因：当前 Wi-Fi 网络连接 GitHub 不稳定，而手机热点可以正常访问。
- [4] day 4 改进了聊天机器人，有了短期和长期记忆，也了解了提示词工程，给AI加入更准确的要求
- [5] day5     
* LangChain 的定位和作用
* ChatOpenAI
* SystemMessage、HumanMessage、AIMessage
* LangChain 版多轮对话
* ChatPromptTemplate
* Prompt 模板变量（如 {question}、{role}、{requirement}）
* LCEL（prompt | model）
* 理解了 LangChain 的模块化和可组合思想