from langchain_deepseek import ChatDeepSeek
from langchain.prompts import PromptTemplate
import os
from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser

load_dotenv()


llm = ChatDeepSeek(
    model = "deepseek-chat",
    api_key = os.getenv("DEEPSEEK_API_KEY")
)

template = "你是一个顶级搞笑小说作家，非常擅长三言两语逗笑读者，你写的小说都非常热门，得到了读者的喜欢。{content}"

prompt = PromptTemplate.from_template(template)

chain = prompt | llm | StrOutputParser()

for chunk in chain.stream({"content": "将一个关于人类登月的搞笑小说。"}):
    print(chunk,end = "",flush = True)



