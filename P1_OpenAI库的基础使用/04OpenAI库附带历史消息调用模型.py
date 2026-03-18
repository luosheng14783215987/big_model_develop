from dotenv import load_dotenv
from openai import OpenAI
import os

load_dotenv()
# 1. 获取client对象，OpenAI类对象
client = OpenAI(
    api_key=os.getenv("DASHSCOPE_API_KEY"),
    base_url=os.getenv("DASHSCOPE_BASE_URL")
)

# 2. 调用模型  等于提供了上下文
response = client.chat.completions.create(
    model="qwen3-max",
    messages=[
        {"role": "system", "content": "你是AI助理，回答很简洁"},
        {"role": "user", "content": "小明有2条宠物狗"},
        {"role": "assistant", "content": "好的"},
        {"role": "user", "content": "小红有3只宠物猫"},
        {"role": "assistant", "content": "好的"},
        {"role": "user", "content": "总共有几个宠物？"}
    ],
    stream=True     # 开启了流式输出的功能
)

# 3. 处理结果
# print(response.choices[0].message.content)
for chunk in response:
    print(
        chunk.choices[0].delta.content,
        end=" ",        # 每一段之间以空格分隔
        flush=True      # 立刻刷新缓冲区
    )
