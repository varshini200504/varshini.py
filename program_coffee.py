import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Sample data with 20 entries
data = {
    'customer_id': range(1, 21),
    'purchase_history': [10, 8, 15, 5, 12, 14, 7, 9, 11, 13, 16, 6, 8, 14, 10, 5, 17, 12, 9, 11],
    'waste_amount': [2, 3, 1, 4, 2, 3, 2, 1, 3, 2, 4, 1, 2, 3, 4, 2, 1, 3, 2, 1],
    'price_change': [5, 10, -5, 0, 5, -2, 3, 1, 0, 5, -3, 2, 4, -1, 0, 5, -4, 2, 3, 1],
    'sales_volume': [20, 15, 25, 10, 18, 12, 17, 14, 19, 22, 13, 11, 16, 21, 20, 9, 24, 19, 15, 18],
    'visit_frequency': [5, 4, 6, 3, 5, 7, 4, 3, 6, 5, 8, 3, 5, 7, 6, 4, 8, 6, 5, 4],
    'customer_feedback_score': [4.5, 4.0, 5.0, 3.5, 4.8, 4.2, 4.1, 4.3, 4.4, 4.7, 4.9, 3.8, 4.1, 4.6, 4.5, 3.9, 5.0, 4.4, 4.3, 4.2],
    'social_media_engagement': [50, 40, 70, 20, 60, 55, 30, 45, 50, 65, 75, 25, 35, 60, 55, 30, 80, 50, 40, 60],
    'online_reviews': [4.2, 4.0, 4.8, 3.5, 4.6, 4.3, 4.1, 4.5, 4.4, 4.7, 4.9, 3.8, 4.0, 4.6, 4.5, 3.9, 5.0, 4.4, 4.3, 4.2]
}

df = pd.DataFrame(data)

# Save DataFrame to CSV file
df.to_csv('customer_data.csv', index=False)
print("CSV file created successfully!")

# Customer Loyalty Analysis
def analyze_customer_loyalty(df):
    df['loyalty_score'] = df['purchase_history'] / df['purchase_history'].sum()
    print("\nCustomer Loyalty Analysis:")
    print(df[['customer_id', 'loyalty_score']])
    plt.figure(figsize=(12, 6))
    sns.barplot(x='customer_id', y='loyalty_score', hue='customer_id', data=df, palette='viridis', legend=False)
    plt.title('Customer Loyalty Analysis')
    plt.xlabel('Customer ID')
    plt.ylabel('Loyalty Score')
    plt.show()

# Waste Reduction Analysis
def analyze_waste_reduction(df):
    print("\nWaste Reduction Analysis:")
    print(df[['customer_id', 'waste_amount']])
    plt.figure(figsize=(12, 6))
    sns.lineplot(x='customer_id', y='waste_amount', data=df, marker='o', linestyle='-', color='b')
    plt.title('Waste Reduction Analysis')
    plt.xlabel('Customer ID')
    plt.ylabel('Waste Amount')
    plt.show()

# Price Sensitivity Analysis
def analyze_price_sensitivity(df):
    print("\nPrice Sensitivity Analysis:")
    print(df[['price_change', 'sales_volume']])
    plt.figure(figsize=(12, 6))
    sns.scatterplot(x='price_change', y='sales_volume', data=df, hue='customer_id', palette='coolwarm', s=100)
    plt.title('Price Sensitivity Analysis')
    plt.xlabel('Price Change')
    plt.ylabel('Sales Volume')
    plt.show()

# Detailed Customer Loyalty Analysis
def detailed_customer_loyalty_analysis(df):
    df['visit_loyalty'] = df['visit_frequency'] / df['visit_frequency'].sum()
    df['feedback_loyalty'] = df['customer_feedback_score'] / df['customer_feedback_score'].sum()
    df['overall_loyalty'] = (df['loyalty_score'] + df['visit_loyalty'] + df['feedback_loyalty']) / 3

    print("\nDetailed Customer Loyalty Analysis:")
    print(df[['customer_id', 'overall_loyalty']])
    plt.figure(figsize=(12, 6))
    sns.barplot(x='customer_id', y='overall_loyalty', hue='customer_id', data=df, palette='magma', legend=False)
    plt.title('Detailed Customer Loyalty Analysis')
    plt.xlabel('Customer ID')
    plt.ylabel('Overall Loyalty Score')
    plt.show()

# Digital Presence Analysis
def analyze_digital_presence(df):
    print("\nDigital Presence Analysis:")
    print(df[['customer_id', 'social_media_engagement', 'online_reviews', 'sales_volume']])
    plt.figure(figsize=(12, 6))
    sns.scatterplot(x='social_media_engagement', y='sales_volume', data=df, hue='online_reviews', palette='viridis', s=100)
    plt.title('Impact of Social Media and Online Reviews on Sales')
    plt.xlabel('Social Media Engagement')
    plt.ylabel('Sales Volume')
    plt.show()

# Analyze Customer Loyalty
analyze_customer_loyalty(df)

# Analyze Waste Reduction
analyze_waste_reduction(df)

# Analyze Price Sensitivity
analyze_price_sensitivity(df)

# Detailed Customer Loyalty Analysis
detailed_customer_loyalty_analysis(df)

# Analyze Digital Presence
analyze_digital_presence(df)
