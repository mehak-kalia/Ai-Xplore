# AnalyticsAgent 🤖
**An agentic AI system that understands your data and talks to you about it.**

Upload any CSV or Excel file → AnalyticsAgent automatically profiles it, detects patterns and anomalies, suggests what's worth exploring, and answers your questions in plain English — all running fully local on your machine. No cloud. No API keys. No cost.

---

## Demo
> *"Which columns have the most outliers?"*
> *"Summarise this dataset for me."*
> *"What's the trend in column X over time?"*

Just upload your file and ask.

---

## What it does

- 🔍 **Auto-profiles any dataset** — shape, distributions, correlations, missing values, and outliers summarised in plain English the moment you upload
- 🚨 **Detects anomalies** — flags unusual patterns in your numeric columns automatically
- 💡 **Suggests analyses** — LLM reads your data and recommends what's worth exploring
- 💬 **Answers natural language questions** — ask anything, get back a chart + plain English explanation
- 🧠 **Remembers past analyses** — FAISS memory lets the agent reference previous findings for richer, context-aware answers

---

## How it works

```
Upload CSV / Excel
        ↓
ProfilerAgent     →    understands your data structure & statistics
        ↓
AnomalyAgent      →    detects unusual patterns & outliers
        ↓
InsightAgent      →    generates plain English explanation + chart
        ↓
Ask follow-up questions → agent answers using FAISS memory
```

---

## Tech Stack

| Layer | Tools |
|---|---|
| LLM (fully local) | LLaMA3 via Ollama |
| Agent Framework | LangGraph + LangChain |
| Memory / RAG | FAISS + sentence-transformers |
| Anomaly Detection | Isolation Forest · Scikit-Learn |
| Data Processing | Pandas · DuckDB |
| Visualisation | Plotly |
| UI | Streamlit |

---

## Quickstart

**1. Prerequisites — install Ollama**

Download from [https://ollama.com/download](https://ollama.com/download) and open the app so the menu bar icon is visible.

```bash
ollama pull llama3.2:3b
```

**2. Clone & setup**

```bash
git clone https://github.com/mehak-kalia/AnalyticsAgent
cd AnalyticsAgent

python3 -m venv venv
source venv/bin/activate        # Mac / Linux
# venv\Scripts\activate         # Windows

pip install -r requirements.txt
```

**3. Run**

```bash
streamlit run app.py
```

Open [http://localhost:8501](http://localhost:8501) in your browser.

---

## Usage

1. Upload any **CSV or Excel** file using the drag-and-drop panel
2. Agent instantly profiles your data and highlights what's interesting
3. Browse the suggested analyses or type your own question
4. Get back **charts + plain English answers**
5. Ask follow-up questions — the agent remembers previous findings

---

## Project Structure

```
AnalyticsAgent/
├── app.py              # Streamlit UI
├── agents.py           # LangGraph agent pipeline
├── anomaly.py          # Isolation Forest anomaly detection
├── memory.py           # FAISS vector memory
├── requirements.txt
├── .gitignore
└── README.md
```

---

## Why fully local?

- ✅ No data leaves your machine
- ✅ No OpenAI API key required
- ✅ No usage cost
- ✅ Works completely offline
- ✅ Safe for sensitive or proprietary datasets

---

## Roadmap

- [x] Auto data profiling
- [x] Anomaly detection
- [x] Natural language Q&A
- [x] FAISS memory across sessions
- [ ] Drag-and-drop CSV / Excel upload
- [ ] Multi-file analysis
- [ ] Export reports as PDF
- [ ] SQL database connections
- [ ] CriticAgent self-correction loop
- [ ] Support for larger models (Mixtral, LLaMA3 70B)

---

## Requirements

```
langchain
langgraph
langchain-community
langchain-core
streamlit
plotly
pandas
scikit-learn
duckdb
faiss-cpu
sentence-transformers
```

---

*Built with LangGraph · LLaMA3 · Ollama · Streamlit · FAISS*
