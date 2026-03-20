# from langchain_community.llms.tongyi import Tongyi
#
# model = Tongyi(model="qwen-max")
#
# # 通过stream方法获得流式输出
# res = model.stream(input="你是谁呀能做什么？")
#
# for chunk in res:
#     print(chunk, end="", flush=True)

from langchain_community.chat_models import ChatTongyi
from langchain_core.messages import HumanMessage

llm = ChatTongyi(
    model="qwen-max",
    streaming=True
)

res = llm.stream([HumanMessage(content="你是谁，能做什么")], streaming=True)
for r in res:
    print(r.content, end="", flush=True)