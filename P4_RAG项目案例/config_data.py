md5_path = "./md5.text"

# Chroma
collection_name = "rag"
persist_directory = "./chroma_db"

# splitter
chunk_size = 1000 # 1000个字符
chunk_overlap = 100 # 重叠100个字符
separators = ["\n\n", "\n", ".", "!", "?", "。", "！", "？", " ", ""]
max_split_char_number=1000

# 向量检索
similarity_threshold = 1  # 每次检索返回文档匹配的数量

# 嵌入模型
embedding_model_name = "text-embedding-v4"
chat_model_name = "qwen3-max"

session_config = {
        "configurable": {
            "session_id": "user_001",
        }
    }
