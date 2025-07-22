import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report

# Load the dataset
df = sns.load_dataset('heart_disease')  # If using seaborn dataset
# df = pd.read_csv("heart_disease.csv")  # If using CSV file

# Task 1: Inspect the data
print(df.head())
print(df.describe())
print(df.info())

# Check missing values
print(df.isnull().sum())

# Task 2: Data Cleaning
# Handle missing data
df.fillna(df.mean(), inplace=True)

# Convert categorical variables to numerical (e.g., one-hot encoding)
df = pd.get_dummies(df, columns=['ChestPainType', 'RestingECG', 'Slope', 'Thal'], drop_first=True)

# Normalize numerical features
scaler = StandardScaler()
df[['Age', 'RestingBP', 'Cholesterol', 'MaxHR', 'Oldpeak']] = scaler.fit_transform(df[['Age', 'RestingBP', 'Cholesterol', 'MaxHR', 'Oldpeak']])

# Task 3: Exploratory Data Analysis
# Univariate distribution of `Age`
sns.histplot(df['Age'], kde=True)
plt.title('Age Distribution')
plt.show()

# Bivariate analysis: `Survived` vs `Sex`
sns.countplot(x='Sex', hue='Target', data=df)
plt.title('Survival by Gender')
plt.show()

# Task 4: Data Aggregation
# Calculate average cholesterol levels for each `Target` (Heart disease presence)
print(df.groupby('Target')['Cholesterol'].mean())

# Task 5: Simple Model (Logistic Regression)
# Prepare data for logistic regression
X = df.drop(columns=['Target'])
y = df['Target']

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize Logistic Regression model
model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)

# Make predictions
y_pred = model.predict(X_test)

# Evaluate the model
print(f'Accuracy: {accuracy_score(y_test, y_pred)}')
print(classification_report(y_test, y_pred))
