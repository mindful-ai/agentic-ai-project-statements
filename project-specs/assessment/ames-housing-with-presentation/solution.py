import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv("AmesHousing.csv")

# Display the first few rows
print("Dataset preview:")
print(df.head())

# Task 1.1: Identify continuous, categorical, and ordinal variables
numerical_features = df.select_dtypes(include=['int64', 'float64']).columns
categorical_features = df.select_dtypes(include=['object']).columns

print("Numerical Features:", list(numerical_features))
print("Categorical Features:", list(categorical_features))

# Task 1.2: Handling Missing Values
missing_values = df.isnull().sum()
missing_values = missing_values[missing_values > 0].sort_values(ascending=False)
print("\nMissing values:\n", missing_values)

# Filling missing values
df['LotFrontage'].fillna(df['LotFrontage'].median(), inplace=True)  # Fill with median
df['GarageType'].fillna('None', inplace=True)  # Fill categorical with 'None'

# Task 1.3: Outliers in Sale Price
plt.figure()
sns.boxplot(x=df['SalePrice'])
plt.title("Boxplot of Sale Price")
plt.show()

# Removing outliers based on 99th percentile
upper_limit = df['SalePrice'].quantile(0.99)
df = df[df['SalePrice'] <= upper_limit]

# Task 2.1: Distribution of Sale Prices by Neighborhood
plt.figure(figsize=(12, 8))
sns.boxplot(data=df, x='Neighborhood', y='SalePrice')
plt.xticks(rotation=90)
plt.title("Sale Price Distribution by Neighborhood")
plt.show()

# Task 2.2: Non-linear Relationships with Sale Price
sns.lmplot(x='GrLivArea', y='SalePrice', data=df, height=7, aspect=1.5,
           line_kws={'color': 'orange'}, scatter_kws={'alpha': 0.3})
plt.title("Sale Price vs. Above Ground Living Area (Non-linear)")
plt.show()

# Task 2.3: Creating New Features
df['HouseAge'] = df['YrSold'] - df['YearBuilt']
sns.scatterplot(data=df, x='HouseAge', y='SalePrice', alpha=0.6)
plt.title("House Age vs Sale Price")
plt.show()

# Task 3.1: Similar-Sized Houses with Different Prices
similar_lot_size = df[(df['LotArea'] > 8000) & (df['LotArea'] < 10000)]
plt.figure(figsize=(10, 6))
sns.scatterplot(data=similar_lot_size, x='LotArea', y='SalePrice', hue='Neighborhood')
plt.title("Sale Price for Similar Lot Sizes Across Neighborhoods")
plt.legend(bbox_to_anchor=(1.05, 1), loc=2)
plt.show()

# Task 3.2: Categorical Variables’ Effect on Sale Price
plt.figure(figsize=(10, 6))
sns.boxplot(data=df, x='SaleCondition', y='SalePrice')
plt.title("Sale Price Distribution by Sale Condition")
plt.show()

# Task 3.3: Seasonal Trends
df['MoSold'] = df['MoSold'].astype('category')
plt.figure(figsize=(10, 6))
sns.boxplot(data=df, x='MoSold', y='SalePrice')
plt.title("Sale Price Distribution by Month Sold")
plt.show()

# Task 4.1: Unique Visualization - Heatmap of Sale Price by Neighborhood and Overall Quality
pivot_table = df.pivot_table(values='SalePrice', index='Neighborhood', columns='OverallQual', aggfunc=np.median)
plt.figure(figsize=(12, 8))
sns.heatmap(pivot_table, annot=True, fmt=".0f", cmap="YlGnBu", cbar_kws={'label': 'Median Sale Price'})
plt.title("Median Sale Price by Neighborhood and Overall Quality")
plt.show()

# Task 4.2: Narrative - Findings for Presentation
print("\nInsights for Presentation:")
print("- Higher median sale prices are found in neighborhoods with better overall quality ratings, suggesting a premium for quality.")
print("- Houses sold under 'Partial' (new constructions) conditions generally have higher sale prices, likely reflecting new builds.")
print("- Noticeable increase in sale prices appears during spring and summer months, likely tied to moving seasons and weather conditions.")

# Task 5: Summarize findings
print("\nWorkshop Complete: Participants can use the above visualizations and insights for storytelling and presentation.")
