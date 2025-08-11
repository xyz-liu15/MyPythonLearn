from langchain_deepseek import ChatDeepSeek
from dotenv import load_dotenv
import os

load_dotenv()


llm = ChatDeepSeek(
    model = "deepseek-chat",
    api_key = os.getenv("DEEPSEEK_API_KEY")
)

result = llm.invoke("你好，deepseek！")

print(result.content)