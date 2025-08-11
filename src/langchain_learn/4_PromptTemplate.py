from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
import os
from rich import print
from langchain_core.prompts import ChatPromptTemplate

api_key = os.getenv("MODELSCOPE_API_KEY")
base_url = os.getenv("MODELSCOPE_BASE_URL")


llm = ChatOpenAI(
    model = "Qwen/Qwen3-Coder-480B-A35B-Instruct",
    api_key = api_key,
    base_url = base_url
)

# 方法一：使用from_template()
template = "你是一个顶级科幻短篇小说作家，极其擅长创作一句话科幻小说，你写的小说都非常热门，得到了读者的喜欢。{content}"

prompt = PromptTemplate.from_template(template)

format_prompt = prompt.format(content = "讲一个关于世界上只剩下一个人类的科幻小说。")
print("===================================================")
print(format_prompt)

chain = prompt | llm

result = chain.invoke({"content": "讲一个关于世界上只剩下一个人类的科幻小说。"})
print("===================================================")
print(result)

# 方法二：使用PromptTemplate中的参数
prompt_variable = PromptTemplate(
    template = "你是一个顶级{type}短篇小说作家，极其擅长创作一句话科幻小说，你写的小说都非常热门，得到了读者的喜欢。{content}",
    input_variables = ["content"],
    partial_variables = {"type": "科幻"}
)

chain_variable = prompt_variable | llm

result_variable = chain_variable.invoke({"content": "地球灾变"})
print("===================================================")
print(result_variable)

result_variable_two = chain_variable.invoke({"content": "人被外星人抓走","type":"仙侠"})
print("===================================================")
print(result_variable_two)


chat_prompt = ChatPromptTemplate.from_messages([
    ("system", "你是一个顶级{type}短篇小说作家，极其擅长创作一句话科幻小说，你写的小说都非常热门，得到了读者的喜欢。"),
    ("human", "{content}")
])