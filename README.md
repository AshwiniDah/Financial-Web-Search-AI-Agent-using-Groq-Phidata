# 🧠 Financial & Web Search AI Agent using Groq + Phidata
This project is an intelligent multi-agent system built using the Phidata framework and powered by Groq-hosted LLaMA 3 models. It combines financial data analysis with real-time web search to generate insights on stocks like NVDIA — including price, fundamentals, and analyst recommendations.

🔧 Features
💹 Finance AI Agent
Uses YFinanceTools to retrieve:

Current stock prices

Key financial fundamentals

🌐## Web Search AI Agent
Uses DuckDuckGo to:

Search the latest news and online content

Automatically include sources for credibility

🤖## Multi-Agent Orchestration
Combines multiple agents (finance + web) to answer complex prompts like:

“Summarize analyst recommendation and share the latest news for NVDIA”

🚀 ##Powered by Groq + LLaMA 3
Ultra-fast response using llama3-groq-70b

🛠️## Tech Stack
Phidata (multi-agent framework)

Groq (high-performance LLM API)

yfinance via phi.tools.YFinanceTools

DuckDuckGo for live web search

Python 3.10+

📦 Setup
## Create virtual environment
```bash
python -m venv venv
source venv/bin/activate   # or venv\Scripts\activate on Windows
```
## Install dependencies
```bash
pip install -r requirements.txt
```

## Run the agent
```bash
python financial_agent.py
```
