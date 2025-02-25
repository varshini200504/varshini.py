import pandas as pd
from sklearn.preprocessing import LabelEncoder
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# Load the dataset
df = pd.read_csv("book2.csv")

# Display first few rows to understand the structure of the dataset
print(df.head())

# Understanding the dataset: Checking data types and structure
print(df.info())

# Checking for missing values in each column
print(df.isnull().sum())

# Encoding categorical variables
df['Brick'] = LabelEncoder().fit_transform(df['Brick'])
df['Neighborhood'] = LabelEncoder().fit_transform(df['Neighborhood'])

# Display the transformed dataset
print(df)

# DATA VISUALIZATION

# House Price Distribution
plt.figure(figsize=(8, 5))
sns.histplot(df["Price"], bins=30, kde=True, color="blue")
plt.title("House Price Distribution")
plt.xlabel("Price")
plt.ylabel("Frequency")
plt.show()

# Feature Correlation Heatmap
plt.figure(figsize=(10, 6))
sns.heatmap(df.corr(), annot=True, cmap="coolwarm", fmt=".2f", linewidths=0.5)
plt.title("Feature Correlation Heatmap")
plt.show()

# Price vs Square Footage
plt.figure(figsize=(8, 5))
sns.scatterplot(x=df["SqFt"], y=df["Price"], alpha=0.6, color="red")
plt.title("Price vs. Square Footage")
plt.xlabel("Square Footage (SqFt)")
plt.ylabel("Price")
plt.show()

# Price vs Number of Bedrooms
plt.figure(figsize=(10,5))
sns.boxplot(x=df["Bedrooms"], y=df["Price"], palette="coolwarm")
plt.title("Price vs. Number of Bedrooms")
plt.xlabel("Number of Bedrooms")
plt.ylabel("Price")
plt.show()

# Average House Price by Neighborhood
plt.figure(figsize=(12, 6))
sns.barplot(x=df["Neighborhood"], y=df["Price"], estimator=np.mean, palette="magma")
plt.xticks(rotation=45)
plt.title("Average House Price by Neighborhood")
plt.xlabel("Neighborhood")
plt.ylabel("Average Price")
plt.show()

# Impact of Brick Houses on Price
plt.figure(figsize=(6, 5))
sns.boxplot(x=df["Brick"], y=df["Price"], palette="coolwarm")
plt.title("Impact of Brick Houses on Price")
plt.xlabel("Brick House (Yes/No)")
plt.ylabel("Price")
plt.show()

# MODELING

# Splitting the data
X = df[['SqFt', 'Bedrooms', 'Brick', 'Neighborhood']]
y = df['Price']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Building the model
model = LinearRegression()
model.fit(X_train, y_train)

# Predicting and evaluating
predictions = model.predict(X_test)
print("Model Coefficients:", model.coef_)
print("Intercept:", model.intercept_)
