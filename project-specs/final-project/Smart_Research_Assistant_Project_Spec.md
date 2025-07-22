
# Capstone Project Specifications

## Project Title
**Smart Research Assistant: Building an RAG-based Agentic AI with LangGraph for Automated Market Intelligence**

---

## Objective
Participants will build an intelligent agent-based system that autonomously collects, processes, analyzes, and responds to market trends using Retrieval-Augmented Generation (RAG) and LangGraph. The system should handle data acquisition, insight extraction, predictive modeling, and dynamic responses using agentic AI principles.

---

## Duration
**50–60 hours of work**

---

## Learning Outcomes
By the end of the project, participants will be able to:

- Collect and process real-world market data from multiple sources
- Build machine learning models for sentiment and trend prediction
- Convert textual insights into vector embeddings and store them in a vector database
- Implement a full RAG pipeline using LangChain tools
- Design and execute agent workflows using LangGraph
- Build a user interface for interacting with the system

---

## Week-wise Plan and Tasks

### Stage 1: Data Collection, Processing & Modeling

#### Task 1: Data Acquisition (Day 1–2)
- Identify and extract data from:
  - TechCrunch (news)
  - Yahoo Finance (stock & financial reports)
  - Amazon Reviews (product sentiment)
  - Reddit (community insights)
  - GDELT (global market trends)
- Use Python, BeautifulSoup, APIs, or LangChain tools (like `RequestsTool`).

#### Task 2: Data Cleaning & Enrichment (Day 3)
- Clean textual data using pandas and regex
- Perform NER (Named Entity Recognition) using spaCy
- Extract keywords and sentiment scores

#### Task 3: ML Model Development (Day 4)
- Build a **Sentiment Classifier** using labeled datasets
- Build a **Trend Forecasting Model** using time-series data
- Save model artifacts for integration

### Stage 2: RAG + Agentic AI with LangGraph

#### Task 4: Embedding and Vector Store (Day 5–6)
- Convert insights into embeddings using OpenAI or BGE
- Store them in a vector database (Chroma, FAISS)
- Include metadata such as source, date, entity, and sentiment

#### Task 5: LangGraph Agent Workflow (Day 7–8)
- Define agent states:
  - `Start → Search → Summarize → Predict → Respond → End`
- Implement nodes using LangGraph
- Integrate LLM, search, prediction, and summarization tools

#### Task 6: ML Model Integration (Day 9)
- Use trained ML models as callable tools inside LangGraph
- The agent should:
  - Search insights
  - Query embeddings
  - Call ML models for prediction
  - Generate answers using RAG

#### Task 7: UI Layer (Optional, Day 10)
- Build a simple front-end using Streamlit or Gradio
- Accept queries like:
  - “What is the market outlook for Nvidia?”
  - “Summarize recent sentiment around Apple’s new launch”

---

## Final Deliverables

1. Cleaned datasets and codebase
2. Trained ML models with evaluation metrics
3. RAG pipeline with LangGraph agents
4. (Optional) UI layer for interaction
5. Project report or presentation (PDF/Slides)
6. GitHub repository with instructions
7. (Optional) Demo video walkthrough

---

## Evaluation Criteria

| Criterion                        | Weight |
|----------------------------------|--------|
| Completeness of Pipeline         | 25%    |
| Quality of ML Model              | 15%    |
| LangGraph Agent Design           | 30%    |
| RAG Integration & Creativity     | 10%    |
| Code Quality & Documentation     | 10%    |
| Final Report & Presentation      | 10%    |

---

# Appendix A: Data Sources

| Source           | Type                  | Usage Example                                                                 |
|------------------|------------------------|--------------------------------------------------------------------------------|
| TechCrunch        | Tech news              | “OpenAI partners with Reddit to boost data quality in ChatGPT”                 |
| Yahoo Finance     | Stock/financials       | “Tesla Q2 earnings beat Wall Street expectations”                             |
| Amazon Reviews    | Customer reviews       | “This laptop is lightweight and fast, ideal for travel.”                      |
| Reddit (PRAW)     | Social discussions     | “Anyone else think Apple Vision Pro is overpriced?”                          |
| GDELT Project     | Global news insights   | “India is becoming a global semiconductor hub.”                               |

Example embedded record:
```json
{
  "text": "Apple launches M4 Ultra AI chip with 5x performance.",
  "entity": "Apple",
  "date": "2025-07-20",
  "tags": ["product launch", "AI", "semiconductors"],
  "embedding": <vector>
}
```

---

# Appendix B: ML Data Specifications

## 1. Sentiment Classification

| Field             | Description                               |
|-------------------|-------------------------------------------|
| text              | Input text (news/review/post)             |
| sentiment_label   | Positive, Neutral, Negative               |
| source            | Origin of data                            |
| entity            | Company or product                        |
| date              | Date of record                            |

Example:
```json
{
  "text": "Tesla's Q2 sales hit record highs.",
  "sentiment_label": "positive",
  "entity": "Tesla",
  "source": "Yahoo Finance",
  "date": "2025-07-15"
}
```

## 2. Trend Prediction

| Field                  | Description                                      |
|------------------------|--------------------------------------------------|
| entity                 | Product/company                                  |
| date                   | Daily/weekly record                              |
| daily_mentions         | Mentions across platforms                        |
| avg_sentiment_score    | Aggregated sentiment from recent insights        |
| engagement_metric      | Upvotes, likes, reviews, etc.                    |
| actual_trend_label     | High, Medium, Low trend                          |

## 3. Event Extraction / NER

| Field         | Description                               |
|---------------|-------------------------------------------|
| text          | Raw news or article                       |
| entities      | Company or person mentioned               |
| event_type    | e.g., Acquisition, Launch, Investment     |
| date          | Publication date                          |

## 4. Market Opportunity Scoring

| Field                  | Description                                      |
|------------------------|--------------------------------------------------|
| product_or_market      | e.g., Edge AI chips                              |
| mentions_growth        | % change over last period                        |
| positive_sentiment_ratio | Fraction of positive mentions                 |
| global_coverage        | # of countries mentioned                         |
| recent_events_count    | # of related launches/news items                 |
| opportunity_score      | 0–1 score (can be generated or labeled)          |

---

## Appendix C: Example Queries for the Assistant

- “Summarize AI investments in the last 30 days.”
- “Show the sentiment trend for Tesla this month.”
- “What’s the opportunity outlook for Quantum Computing?”
- “Compare mentions and sentiment of Google and Microsoft.”
