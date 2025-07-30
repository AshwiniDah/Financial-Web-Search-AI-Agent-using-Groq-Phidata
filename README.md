# 🧠 Financial & Web Search AI Agent using Groq + Phidata
This project is an intelligent multi-agent system built using the Phidata framework and powered by Groq-hosted LLaMA 3 models. It combines financial data analysis with real-time web search to generate insights on stocks like NVDIA — including price, fundamentals, and analyst recommendations.

### 🔧 Features
💹 Finance AI Agent
Uses YFinanceTools to retrieve:
Current stock prices
Key financial fundamentals

### 🌐 Web Search AI Agent
Uses DuckDuckGo to:
Search the latest news and online content
Automatically include sources for credibility

### 🤖 Multi-Agent Orchestration
Combines multiple agents (finance + web) to answer complex prompts like:
“Summarize analyst recommendation and share the latest news for NVDIA”

### ⚡ Powered by Groq + LLaMA 3
Ultra-fast response using llama3-groq-70b 

### 🔐 Required API Keys
To run this project, you’ll need the following API keys:

Service	API Key Name	Where to get it

Phidata	PHI_API_KEY	https://cloud.phidata.com (sign up and get API key)

Groq	GROQ_API_KEY	https://console.groq.com/keys

OpenAI	OPENAI_API_KEY	https://platform.openai.com/account/api-keys

You can set these as environment variables or store them securely in your .env file.

### 🛠️ Tech Stack

Phidata (multi-agent framework)

Groq (high-performance LLM API)

yfinance via phi.tools.YFinanceTools

DuckDuckGo for live web search

Python 3.12

### 📦 Setup

### Create virtual environment
```bash
python -m venv venv
source venv/bin/activate   # or venv\Scripts\activate on Windows
```
### Install dependencies
```bash
pip install -r requirements.txt
```
### 🚀 Run the agent
```bash
# Make sure API keys are set
# Then run:
python financial_agent.py
```
