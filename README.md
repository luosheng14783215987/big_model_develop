# big_model_develop

本仓库是一个**大模型开发学习/案例集合**，按目录分为多个阶段示例（以 Python 脚本为主）。

## 目录结构

- `P1_OpenAI库的基础使用`：使用 `openai` SDK 调用大模型（含流式输出、对话消息等）
- `P2_提示词优化`：提示词优化案例（金融文本分类/抽取/匹配等）
- `P3_LangChainRAG开发`：LangChain 基础与 RAG 相关（Loader、Embedding、向量存储/检索、Chroma 持久化等）
- `P4_RAG项目案例`：预留/项目案例目录（当前可能为空）

## 环境要求

- Python 3.10+（建议 3.11）
- 建议使用虚拟环境（`venv`/`conda` 均可）

## 安装依赖（建议）

本仓库当前未提供统一的依赖清单文件，你可以按需安装（覆盖 P1~P3 常用示例）：

```bash
python -m venv .venv
.venv\Scripts\activate

pip install -U pip
pip install openai python-dotenv langchain langchain-community langchain-core langchain-chroma chromadb pypdf
```

> 说明：`P3_LangChainRAG开发` 中使用了 Chroma 向量库持久化（会生成 `chroma_db` 目录），以及若干文档加载器（如 `CSVLoader`、`PyPDFLoader`）。

## 配置环境变量（强烈建议）

`P1_OpenAI库的基础使用`、`P2_提示词优化` 目录下存在 `.env` 用于读取密钥与接口地址（请勿提交到 Git）。

常见变量（以 DashScope/通义千问为例）：

```env
# API Key（示例名：DASHSCOPE_API_KEY）
DASHSCOPE_API_KEY=your_key_here

# OpenAI SDK 兼容的 base_url（示例名：DASHSCOPE_BASE_URL）
DASHSCOPE_BASE_URL=https://dashscope.aliyuncs.com/compatible-mode/v1
```

> 注意：仓库中个别示例脚本可能包含硬编码 key。**强烈建议你在上传 Git 前将其改为从环境变量读取**，避免泄漏。

## 运行示例

以某个脚本为例：

```bash
python "P1_OpenAI库的基础使用/02OpenAI库的基础使用.py"
```

`P3_LangChainRAG开发` 中涉及本地持久化/数据目录的脚本，请在对应目录下运行（或自行调整脚本里的相对路径）：

```bash
cd "P3_LangChainRAG开发"
python "27外部向量持久化存储.py"
```

## Git 提交建议

- 不要提交：`.env`、`.venv`、`__pycache__`、IDE 工程文件（如 `.idea/`）、本地向量库持久化目录（如 `chroma_db/`）
- 如果你希望让别人一键运行，建议后续补充 `requirements.txt` 或 `pyproject.toml`

