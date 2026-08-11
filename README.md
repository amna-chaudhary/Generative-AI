# 🤖 Generative AI — LangChain Learning Lab

**A hands-on journey through building LLM-powered applications with LangChain**

Practical implementations of chains, models, prompt engineering, RAG pipelines, and runnables — built to master real-world Generative AI development.

---

## 🎯 About This Repository

This repo documents my **structured, hands-on learning path** through LangChain — going from the fundamentals of prompts and chains to building a complete **Retrieval-Augmented Generation (RAG)** pipeline. Every folder represents a core concept in modern LLM application development, implemented and tested with working code.

> Built as part of my journey toward becoming a **Generative AI Engineer**, alongside real-world projects like an AI-driven RAG bot and n8n automation workflows.

---

## 🗂️ What's Inside

### 🔗 Chains
Composing LLM calls into powerful workflows
- `simple_chain_example.py`
- `sequential_chain.py`
- `parallel_chain.py`
- `conditional_chain.py`

### 🧠 Models
Connecting to different LLM providers
- `llm_openai.py`
- `chatmodel_openai.py`
- `huggingface_inference_api.py`
- `huggingface_run_locally.py`

### 📤 OutputParsers
Turning raw LLM text into structured data
- `str-output-parser.py`
- `json-output-parser.py`
- `pydantic-output-parser.py`
- `structured-output-parser.py`

### ✍️ PromptEngineering
Designing effective, reusable prompts
- `static-prompt-practice.py`
- `dynamic-prompt-practice.py`
- `message_placeholder.py`

### ⚙️ Runnables
LangChain's composable execution primitives
- `runnablePassthrough.py`
- `runnableParallel.py`
- `runnableLambda.py`
- `runnableBranch.py`

### 📦 WithStructuredOutput
Enforcing schema-based, validated LLM responses

### 🔍 RAG — Retrieval-Augmented Generation *(Core Module)*

The most in-depth module — a complete RAG pipeline built from the ground up:

```
RAG/
├── DocumentLoaders/        Load data from PDFs, CSVs, text & web pages
│   ├── Files/               (AMNA_BIBI.pdf, currency.csv, sample.txt)
│   ├── csv_loader.py
│   ├── pyppdf_loader.py
│   ├── text_loader.py
│   ├── webbase_loader.py
│   └── directoryloader.py
│
├── TextSplitter/           Chunk documents intelligently
│   ├── lengthbased_splitter.py
│   └── textstructured_splitter.py
│
├── Retrievers/              Fetch relevant context for queries
└── VectorDatabase/          Store & search embeddings
```

---

## 🧭 Learning Path

```
Prompt Engineering → Models → Output Parsers → Chains → Runnables → RAG Pipeline → Structured Output
```

This repo follows a **progressive learning structure** — starting with prompt design fundamentals and building up to a full retrieval-augmented pipeline capable of answering questions from custom documents.

---

## 🛠️ Tech Stack

| Category | Tools |
|---|---|
| **Language** | Python 3.10+ |
| **Framework** | LangChain |
| **LLM Providers** | OpenAI API, HuggingFace (Inference API & local) |
| **Document Sources** | PDF, CSV, TXT, Web pages |
| **Core Concepts** | Chains, Runnables, Output Parsers, RAG, Structured Output |

---

## 🚀 Getting Started

```bash
# 1. Clone the repository
git clone https://github.com/amna-chaudhary/Generative-AI.git
cd Generative-AI

# 2. Create & activate a virtual environment
python -m venv venv
venv\Scripts\activate        # Windows
source venv/bin/activate     # macOS/Linux

# 3. Install dependencies
pip install -r requirements.txt

# 4. Add your API keys in a .env file
# OPENAI_API_KEY=your_key_here
# HUGGINGFACEHUB_API_TOKEN=your_key_here
```

Run any module independently, e.g.:
```bash
python Chains/sequential_chain.py
```

---

## 📌 Why This Repo

This isn't just practice code — it's a **structured reference** I built to deeply understand how production LLM applications are architected, and it directly feeds into my real-world projects (RAG bots, AI agents, automation workflows). Feel free to explore, fork, or reach out if you'd like to collaborate.

---

## 👩‍💻 Author

**Amna Chaudhary**
Generative AI Engineer | LangChain • RAG • LLM Integrations

GitHub: [amna-chaudhary](https://github.com/amna-chaudhary)

⭐ *If this repo helped you, consider giving it a star!*
