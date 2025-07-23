# Project Specification: Product Rating Classification

## Title
**Product Rating Classification: Predicting Product Ratings from Reviews and Metadata**

## Objective
To classify product ratings (e.g., 1 to 5 stars) based on customer reviews and structured metadata using a combination of text preprocessing, feature engineering, and machine learning models.

## Suggested Dataset
Use the **Amazon Product Review Dataset** (available on Kaggle or AWS Open Data Registry). Select a subset such as Electronics, Books, or Clothing.

Link: [Amazon Reviews Dataset on Kaggle](https://www.kaggle.com/datasets/bittlingmayer/amazonreviews)

---

## Project Tasks

### Task 1: Data Understanding and Loading
- Load the dataset using pandas.
- Explore the columns: e.g., `reviewText`, `overall` (rating), `summary`, `verified`, `category`, `price`, etc.
- Display sample rows and value counts.

### Task 2: Text Cleaning
- Remove punctuation from `reviewText` and `summary`.
- Convert text to lowercase.
- Remove stop words using NLTK or spaCy.
- Optionally apply lemmatization.

### Task 3: Feature Engineering
- **Text Features:**
  - Length of the review text.
  - Word count.
  - Presence of keywords (e.g., “excellent”, “bad”, “broken”).
- **Structured Features:**
  - Convert `verified` to binary.
  - Handle missing values in `price`, fill or drop as needed.

### Task 4: Encoding Categorical Variables
- Label encode columns like `category`.
- One-hot encode if the number of categories is limited.

### Task 5: Vectorization of Text Data
- Use `CountVectorizer` and `TfidfVectorizer` from `sklearn`.
- Apply to `reviewText` or `summary`.
- Combine with other numerical/categorical features using `hstack` or `ColumnTransformer`.

### Task 6: Model Building
- Split the data into train-test sets.
- Try classifiers: Logistic Regression, Random Forest, XGBoost.
- Train and evaluate using accuracy, F1-score, confusion matrix.

### Task 7: Interpretability
- Use `eli5`, SHAP, or `sklearn`’s `feature_importances_` for model interpretation.
- Identify which words or features contribute most to rating prediction.

### Task 8: Summary and Improvements
- Summarize findings.
- Recommend improvements such as BERT-based modeling or feature selection.

---

## Deliverables
- Cleaned dataset (optional CSV)
- Jupyter Notebook or Python script
- PDF report (optional)
- Plots: Confusion matrix, feature importance chart, vectorizer examples

---

## Appendix
- Tools: Pandas, Numpy, Scikit-learn, NLTK/spaCy, Matplotlib/Seaborn, ELI5/SHAP
- Skills: Data preprocessing, vectorization, classification, model evaluation, explainability