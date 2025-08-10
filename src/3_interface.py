from langchain_deepseek import ChatDeepSeek
from langchain.prompts import PromptTemplate
import os
from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser
from rich import print
from langchain_core.runnables import RunnableLambda, RunnableParallel, RunnablePassthrough
from pathlib import Path


load_dotenv()


llm = ChatDeepSeek(
    model = "deepseek-chat",
    api_key = os.getenv("DEEPSEEK_API_KEY")
)

template = "你是一个顶级搞笑小说作家，非常擅长在50字内逗笑读者，你写的小说都非常热门，得到了读者的喜欢。{content}"

prompt = PromptTemplate.from_template(template)

chain = prompt | llm | StrOutputParser()
# stream 实时流式输出
for chunk in chain.stream({"content": "讲一个关于人类登月的搞笑小说。"}):
    print(chunk,end = "",flush = True)

print("\n======================================================================================")

# invoke 调用
result = chain.invoke({"content": "讲一个关于后裔射日的搞笑小说。"})
print(result)

print("======================================================================================")


# batch 批量调用
results = chain.batch([
    {"content": "讲一个关于嫦娥奔月的搞笑小说。"},
    {"content": "讲一个关于吴刚砍树的搞笑小说。"},
    {"content": "讲一个关于月兔吃草的搞笑小说。"},
    {"content": "讲一个关于夸父追日的搞笑小说。"},
])
print(results)

# Runnable 对象
# 1. RunnablePassthrough 
chain_passthrough = RunnablePassthrough() | prompt | llm | StrOutputParser()
print(chain_passthrough.invoke({"content": "讲一个关于人类登月的搞笑小说。"}))
  
# 方法assgin()
chain_assign = RunnablePassthrough.assign(content = lambda x: "讲一个关于" + x["content"] + "的搞笑小说。") | prompt | llm | StrOutputParser()
print(chain_assign.invoke({"content": "吴刚"}))

chain_plus = (
    {"today" : RunnableLambda(lambda x: "今天是" + x["content"])}
)

parallel = RunnableParallel(
    chain_1 = chain,
    chain_2 = chain_plus
)

print(parallel.invoke({"content": "2023年10月10日"}))