from langchain_core.prompts import PromptTemplate
from langchain_community.chat_models.tongyi import ChatTongyi
# zero-shot
prompt_template = PromptTemplate.from_template(
    "我的邻居姓{lastname}, 刚生了{gender}, 你帮我起个名字，简单回答。"
)

# 得到模型对象, qwen3-max就是聊天模型
model = ChatTongyi(model="qwen3-max",
                   dashscope_api_key="sk-bab541fb2b874b70abff4a4a1d53861f")
# 调用.format方法注入信息即可
# prompt_text = prompt_template.format(lastname="张", gender="女儿")

# model = Tongyi(model="qwen-max")
# res = model.invoke(input=prompt_text)
# print(res.content)

chain = prompt_template | model
#
res = chain.invoke(input={"lastname": "张", "gender": "女儿"})
print(res)
