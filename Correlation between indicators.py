import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load your data into a DataFrame
df = pd.read_csv(r'C:\Users\USER\Documents\WORK\ME\Shiva\NEW\World Per capita electricity consumption.csv')

# Select only numeric columns for correlation
numeric_columns = df.select_dtypes(include=['float64', 'int64']).columns
numeric_df = df[numeric_columns]

# Calculate correlations between numeric columns
correlation_matrix = numeric_df.corr()

# Visualize the correlation matrix
plt.figure(figsize=(12, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f")
plt.title('Correlation Matrix')
plt.show()

# Assuming you have a column for 'Year' in your DataFrame
time_correlation = df.groupby('Year').corr()

# Visualize the time-wise correlation matrix
plt.figure(figsize=(12, 8))
sns.heatmap(time_correlation, annot=True, cmap='coolwarm', fmt=".2f")
plt.title('Time-wise Correlation Matrix')
plt.show()
