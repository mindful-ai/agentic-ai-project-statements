import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelEncoder

# Load the dataset
auto_data = sns.load_dataset('mpg')  # If using seaborn dataset
# auto_data = pd.read_csv('automobile.csv')  # If using CSV file

# Task 1: Inspect the Data
print(auto_data.head())
print(auto_data.describe())
print(auto_data.info())

# Check for missing values
print(auto_data.isnull().sum())

# Task 2: Data Cleaning
# Handle missing data
auto_data['horsepower'] = pd.to_numeric(auto_data['horsepower'], errors='coerce')
auto_data.fillna(auto_data.median(), inplace=True)

# Convert 'origin' to categorical
auto_data['origin'] = auto_data['origin'].map({1: 'USA', 2: 'Europe', 3: 'Japan'})

# Feature Engineering
auto_data['weight_per_cylinder'] = auto_data['weight'] / auto_data['cylinders']
auto_data['mpg_per_horsepower'] = auto_data['mpg'] / auto_data['horsepower']

# Task 3: Univariate Analysis
# Distribution of mpg
sns.histplot(auto_data['mpg'], kde=True)
plt.title('Distribution of Miles per Gallon (mpg)')
plt.show()

# Boxplot for Horsepower
sns.boxplot(x='horsepower', data=auto_data)
plt.title('Horsepower Distribution')
plt.show()

# Bivariate Analysis
# Scatter plot: mpg vs horsepower
sns.scatterplot(x='horsepower', y='mpg', data=auto_data)
plt.title('mpg vs Horsepower')
plt.show()

# Scatter plot: mpg vs weight
sns.scatterplot(x='weight', y='mpg', data=auto_data)
plt.title('mpg vs Weight')
plt.show()

# Correlation heatmap
corr_matrix = auto_data.corr()
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', fmt='.2f')
plt.title('Correlation Matrix')
plt.show()

# Task 4: Data Aggregation and Grouping
# Average mpg by origin and cylinders
mpg_by_origin_cylinders = auto_data.groupby(['origin', 'cylinders'])['mpg'].mean().reset_index()
sns.barplot(x='origin', y='mpg', hue='cylinders', data=mpg_by_origin_cylinders)
plt.title('Average mpg by Origin and Cylinders')
plt.show()

# Task 5: Advanced Visualizations
# Pairplot of key numerical features
sns.pairplot(auto_data[['mpg', 'horsepower', 'weight', 'displacement']])
plt.title('Pairplot of Numerical Features')
plt.show()

# Facet grid to compare mpg by origin
g = sns.FacetGrid(auto_data, col="origin")
g.map(sns.scatterplot, 'weight', 'mpg')
plt.title('mpg vs Weight by Origin')
plt.show()

# 3D Scatter plot (optional - requires plotly)
import plotly.express as px
fig = px.scatter_3d(auto_data, x='horsepower', y='weight', z='mpg', color='origin')
fig.update_layout(title="3D Scatter Plot of mpg vs Horsepower vs Weight")
fig.show()
