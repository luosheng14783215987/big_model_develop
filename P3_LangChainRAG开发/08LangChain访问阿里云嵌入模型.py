from langchain_community.embeddings import DashScopeEmbeddings

# 创建模型对象 不传model默认用的是 text-embeddings-v1
model = DashScopeEmbeddings(dashscope_api_key="sk-bab541fb2b874b70abff4a4a1d53861f")

# 不用invoke stream
# embed_query、embed_documents
print(model.embed_query("我喜欢你"))
print(model.embed_documents(["我喜欢你", "我稀饭你", "晚上吃啥"]))
