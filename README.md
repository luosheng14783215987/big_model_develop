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
pip install openai langchain langchain-community langchain-core langchain-chroma chromadb pypdf
```

> 说明：`P3_LangChainRAG开发` 中使用了 Chroma 向量库持久化（会生成 `chroma_db` 目录），以及若干文档加载器（如 `CSVLoader`、`PyPDFLoader`）。

## 配置环境变量（系统/外部环境）

本仓库示例通过 **操作系统环境变量** 读取配置（不使用 `.env` 文件）。请在运行前自行设置，例如：

| 变量名 | 说明 |
|--------|------|
| `OPENAI_API_KEY` | **P1 / P2**：官方 `openai` SDK 默认读取的密钥（请填 DashScope/百炼 的 API Key，与控制台密钥相同） |
| `DASHSCOPE_BASE_URL` | **P1 / P2**：兼容模式地址，如 `https://dashscope.aliyuncs.com/compatible-mode/v1` |
| `DASHSCOPE_API_KEY` | **P3 / P4**：LangChain 的 `ChatTongyi`、`DashScopeEmbeddings` 等默认读取的密钥 |

> 建议：将 `OPENAI_API_KEY` 与 `DASHSCOPE_API_KEY` 设为**同一串 API Key**，这样 P1～P4 无需改代码即可跑通。

**Windows（当前会话）示例：**

```powershell
$env:OPENAI_API_KEY = "你的Key"
$env:DASHSCOPE_API_KEY = "你的Key"
$env:DASHSCOPE_BASE_URL = "https://dashscope.aliyuncs.com/compatible-mode/v1"
```

**Linux / macOS 示例：**

```bash
export OPENAI_API_KEY="你的Key"
export DASHSCOPE_API_KEY="你的Key"
export DASHSCOPE_BASE_URL="https://dashscope.aliyuncs.com/compatible-mode/v1"
```

> P1/P2 的 `OpenAI(...)` **不显式传入 `api_key`**，由 SDK 从 `OPENAI_API_KEY` 读取；P3/P4 的通义组件从 `DASHSCOPE_API_KEY` 读取（代码中不写 `dashscope_api_key` 参数）。

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

- 不要提交：`.venv`、`__pycache__`、IDE 工程文件（如 `.idea/`）、本地向量库持久化目录（如 `chroma_db/`）、以及任何含密钥的本地配置文件（若你自行使用 `.env` 等，勿提交）
- 如果你希望让别人一键运行，建议后续补充 `requirements.txt` 或 `pyproject.toml`

