
# Project Specification: Conversational Agents in Finance
## Title: Automating Portfolio Analysis with Agentic AI

### Objective
To design and implement an agentic AI system that functions as a conversational assistant for financial portfolio analysis. The assistant should be able to ingest, reason over, and respond intelligently to user queries regarding asset allocation, portfolio diversification, risk profiles, and investment strategies using a combination of RAG (Retrieval-Augmented Generation) and LangGraph-powered agents.

---

## Project Tasks and Timeline

### Task 1: Data Collection and Preprocessing (Week 1)
- **Objective:** Collect and preprocess structured and unstructured financial data.
- **Data Sources:**
  - Yahoo Finance API (stock prices, market cap, P/E ratios)
  - Financial Modeling Prep API (fundamentals, analyst ratings)
  - SEC EDGAR Filings (10-K, 10-Q for companies)
  - Financial news sources (e.g., Reuters, Bloomberg)
  - Investment strategy blogs and whitepapers
- **Deliverables:**
  - Scripted pipelines for fetching structured data (CSV, JSON)
  - Crawled/cleaned financial text documents for RAG
  - Data storage schema and organization

### Task 2: Financial Knowledge Embedding (Week 2)
- **Objective:** Convert financial texts into vector representations for semantic retrieval.
- **Steps:**
  - Use financial-domain-specific LLM embeddings (e.g., FinBERT, OpenAI Embeddings)
  - Chunk and embed financial news, filings, and blogs
  - Store embeddings in vector database (e.g., FAISS, ChromaDB, Weaviate)
- **Deliverables:**
  - Vector DB with embedded knowledge base
  - Retrieval query test scripts

### Task 3: Building Predictive Financial Models (Week 3)
- **Objective:** Build models for predicting stock movement, volatility, and portfolio returns.
- **Examples of Predictive Models:**
  - Stock price movement (classification/regression)
  - Portfolio return estimation (XGBoost/LightGBM/Linear Regression)
  - Risk clustering (KMeans/hierarchical clustering)
- **Data Required:**
  - Historical stock prices
  - Fundamental ratios (P/E, debt-equity, ROI, etc.)
  - Macroeconomic indicators (interest rates, GDP, CPI)
- **Deliverables:**
  - Trained models with evaluation reports
  - Sample inferences on user-uploaded portfolios

### Task 4: RAG-Based Agentic AI System (Week 4)
- **Objective:** Integrate LangGraph agents with vector search to create a conversational financial assistant.
- **Steps:**
  - Build sub-agents (Retriever, Analyzer, Summarizer, Reporter)
  - Chain agents with LangGraph to reason over portfolios
  - Add prompt templates for query types (e.g., “Summarize risk”, “Compare portfolios”)
  - Enable memory for contextual Q&A
- **Deliverables:**
  - LangGraph-powered agentic assistant
  - Query interface (CLI or Streamlit UI)

### Task 5: User Interface and Demonstration (Week 5)
- **Objective:** Create a professional, simple interface for testing the assistant.
- **Steps:**
  - Design with Streamlit or LangChain UI
  - Upload CSV portfolio and ask financial questions
  - Enable explanations of strategy, diversification, risk, and return
- **Deliverables:**
  - Working demo with upload, chat, and visualization
  - Screencast or live demo presentation

---

## Evaluation Criteria
- Quality of data pipeline and embeddings
- Effectiveness of ML models (RMSE, accuracy, etc.)
- Intelligence and modularity of agentic architecture
- Usability and interactivity of final application
- Documentation and presentation quality

---

## Appendices

### Appendix A: Suggested Tools and Libraries
- **Data:** yfinance, pandas, requests, BeautifulSoup
- **ML:** scikit-learn, XGBoost, LightGBM
- **RAG:** LangChain, OpenAI API, FAISS
- **Agents:** LangGraph, GPT-4, ReAct, Memory module
- **UI:** Streamlit, Flask (optional)

### Appendix B: Sample Prompts
- “Summarize risk factors in my portfolio.”
- “What are the diversification gaps?”
- “Predict returns for the next quarter.”
- “Compare my portfolio to S&P 500.”

### Appendix C: Expected Directory Structure
```
project-root/
├── data/
│   ├── raw/
│   └── processed/
├── models/
├── agents/
├── ui/
├── embeddings/
├── vector_db/
└── main.py
```
