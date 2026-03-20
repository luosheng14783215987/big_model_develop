# langchain_community
from langchain_community.chat_models import ChatTongyi

# 密钥从环境变量 DASHSCOPE_API_KEY 读取（勿在代码中写死）
llm = ChatTongyi(model="qwen-max")

res = llm.invoke("Why do parrots talk?")
print(res.content)