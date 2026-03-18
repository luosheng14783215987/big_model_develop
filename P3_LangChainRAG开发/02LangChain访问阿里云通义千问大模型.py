# langchain_community
from langchain_community.chat_models import ChatTongyi

llm = ChatTongyi(
    model="qwen-max",
    dashscope_api_key="sk-bab541fb2b874b70abff4a4a1d53861f",
)

res = llm.invoke("Why do parrots talk?")
print(res.content)