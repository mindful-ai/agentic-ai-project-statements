# Project: Email Spam Classification + Response Time Regression

## Project Overview

This guided project aims to demonstrate the application of both classification and regression using real-world email data. The objective is two fold:

1. **Email Spam Classification** – Classify emails as `spam` or `ham`.
2. **Response Time Regression** – Predict the response time (in minutes) for non-spam emails.

Students will:
- Perform post-NLP training text processing
- Use traditional ML models and a neural network model
- Compare results using different metrics
- Build a FastAPI application for prediction
- Containerize the solution using Docker
- Test it using Python scripts

---

## Dataset

Use the **Enron-Spam Email Dataset** or the **SpamAssassin Public Corpus**, augmented with synthetic `response_time` values.

### Suggested Dataset Source:
- [Enron Email Dataset with spam labels](https://www.kaggle.com/datasets/wcukierski/enron-email-dataset)
- Generate synthetic `response_time` for non-spam emails using random values (e.g., 5 to 1440 minutes)

---

## Project Tasks

### 1. Data Preprocessing

- Load dataset using `pandas`
- Remove duplicates and nulls
- For spam classification, use label `spam` = 1, `ham` = 0
- For regression, only use `ham` emails and synthesize a `response_time` column

### 2. Text Cleaning (Post-NLP)

- Convert text to lowercase
- Remove punctuation
- Remove stop words
- Apply stemming/lemmatization (NLTK/spaCy)

### 3. Feature Engineering

- Add new columns:
  - Email length
  - Number of words
  - Count of exclamation/question marks
  - Keyword counts (e.g., "urgent", "money", "free")

### 4. Encoding Non-text Features

- If available, one-hot encode sender domain, subject length bucket, etc.
- Label encode categorical fields if necessary

### 5. Text Vectorization

- Use `CountVectorizer` and `TF-IDF Vectorizer` separately
- Combine with engineered features using `hstack` or `pandas.concat`

### 6. Train-Test Split

- Use 80-20 split
- Maintain separate datasets for classification and regression tasks

---

## Model Building

### A. Classification (Spam Detection)

#### Traditional ML Models:
- Logistic Regression
- Naive Bayes
- Random Forest

#### Neural Network Model:
- Input: Vectorized email + features
- Layers: Dense(128) → Dropout → Dense(64) → Output(Sigmoid)

#### Metrics:
- Accuracy
- Precision, Recall, F1
- Confusion Matrix

---

### B. Regression (Response Time)

#### Traditional ML Models:
- Linear Regression
- Random Forest Regressor

#### Neural Network Model:
- Input: Vectorized + numerical features
- Layers: Dense(128) → Dropout → Dense(64) → Output(1 unit)

#### Metrics:
- RMSE
- MAE
- R² score

---

## Interpretation

- Use `eli5`, `SHAP`, or `feature_importances_` to explain important features
- Show keyword contributions to prediction (word clouds)

---

## FastAPI App

### Features:
- `/predict_spam`: Accepts email body, returns spam/ham prediction
- `/predict_response_time`: Accepts email body (only ham), returns response time in minutes

### Requirements:
- Use `joblib` or `pickle` to load ML/NN models
- Integrate preprocessing and vectorization inside API

---

## Dockerize the App

1. **Create Dockerfile**:
   - Base image: `python:3.10`
   - Copy app files
   - Install `requirements.txt`
   - Expose port `8000`
   - CMD: `uvicorn main:app --host 0.0.0.0 --port 8000`

2. **Build and Run Docker Container**:
   ```bash
   docker build -t email-api .
   docker run -p 8000:8000 email-api

## Test using python script

### Sample

```python
import requests

# Test spam prediction
resp = requests.post("http://localhost:8000/predict_spam", json={"email_text": "You won free cash now!"})
print(resp.json())

# Test response time prediction
resp = requests.post("http://localhost:8000/predict_response_time", json={"email_text": "Can we meet at 4pm?"})
print(resp.json())
```