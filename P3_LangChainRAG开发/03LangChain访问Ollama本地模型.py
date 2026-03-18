# langchain_ollama
from langchain_ollama import OllamaLLM

from langchain_community.chat_models import ChatTongyi

llm = ChatTongyi(
    model="qwen3:4b"
)

res = llm.invoke("Why do parrots talk?")
print(res.content)