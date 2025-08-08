from langchain_deepseek import ChatDeepSeek
from langchain.prompts import PromptTemplate
import os
from dotenv import load_dotenv


load_dotenv()


llm = ChatDeepSeek(
    model = "deepseek-chat",
    api_key = os.getenv("DEEPSEEK_API_KEY")
)

prompt = PromptTemplate(
    input_variables=["product"],
    template="你好，deepseek！我想知道{product}的价格。",
)

result = llm.invoke(prompt.format(product="iPhone"))



print(result.content)



