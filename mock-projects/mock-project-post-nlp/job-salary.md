# Project Specification: Job Salary Prediction and Role Classification

## Objective

Develop a dual-purpose machine learning and deep learning system:
- **Regression**: Predict the salary of a job posting
- **Classification**: Classify the role/category of the job posting

You will explore:
- Text preprocessing (post-NLP)
- Feature engineering
- Building ML and Neural Network models
- Building a FastAPI app
- Dockerizing the app
- Testing with sample input

---

## Dataset

### Suggested Dataset:
- **Source**: [Kaggle - Job Salary Prediction](https://www.kaggle.com/datasets/madhab/jobposts)
- **Fields** (sample):
  - `Title`: Job title
  - `Company`: Company name
  - `Location`: Job location
  - `FullDescription`: Full job description (text-heavy)
  - `ContractType`: Full-time, part-time
  - `ContractTime`: Permanent, temporary
  - `Category`: Job category (target for classification)
  - `SalaryNormalized`: Target variable for regression

---

## Phase 1: Data Preprocessing

### 1. Text Cleaning (on `FullDescription`)
- Convert to lowercase
- Remove punctuation
- Remove stopwords
- Optional: Stemming or Lemmatization

### 2. Feature Engineering
- Length of description
- Word count
- Count of specific keywords (e.g., “remote”, “python”, “sql”)
- Number of capitalized words

### 3. Encode Categorical Variables
- One-hot encode `ContractType`, `ContractTime`, `Location`
- Label encode `Category` (for classification target)

---

## Phase 2: Text Vectorization

Apply on cleaned `FullDescription`:
- **Option 1**: CountVectorizer
- **Option 2**: TF-IDF Vectorizer
- Limit features (e.g., `max_features=5000`)

Combine these vectors with other features (e.g., keyword counts, length) using `hstack`.

---

## Phase 3: Modeling

### A. Machine Learning Models

#### 1. Regression Task (Salary)
- Linear Regression
- Random Forest Regressor
- Gradient Boosting Regressor

#### 2. Classification Task (Role)
- Logistic Regression
- Random Forest Classifier
- XGBoost Classifier

Evaluate:
- **Regression**: MAE, RMSE, R²
- **Classification**: Accuracy, Precision, Recall, F1-score

### B. Neural Network Models

Use Keras or PyTorch.

#### 1. Build two models:
- Model 1: Predict salary (regression head)
- Model 2: Predict job category (classification head)

Use:
- Embedding layer or pre-vectorized inputs
- Dense layers
- Regularization and dropout
- ReLU activations

Compare performance of neural models with traditional ML.

---

## Phase 4: Model Interpretability

- Feature Importance from ML models (e.g., using `feature_importances_`)
- SHAP or LIME for neural networks (optional, advanced)

---

## Phase 5: FastAPI Application

### 1. API Features
- Accept new job post input (title, description, etc.)
- Predict both salary and category
- Return predictions as JSON

### 2. Implementation Steps
- Use FastAPI to define `/predict` endpoint
- Load trained ML/NN models
- Accept input as JSON and return output

---

## Phase 6: Dockerization

### 1. Dockerfile
```dockerfile
FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]

### 2. Build and run

```bash
docker build -t job-salary-role-predictor .
docker run -p 8000:8000 job-salary-role-predictor

```

## Phase 7: Test with python

```python

import requests

url = "http://localhost:8000/predict"
data = {
    "Title": "Senior Data Scientist",
    "FullDescription": "Looking for a senior data scientist with 5+ years of experience in ML, NLP, and deep learning. Must know Python and SQL.",
    "Location": "London",
    "ContractType": "permanent",
    "ContractTime": "full_time"
}

response = requests.post(url, json=data)
print(response.json())

```