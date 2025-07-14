import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load your cleaned data
load = pd.read_csv('research-and-development-survey-2024.csv')
# Step 1: Convert to numeric (invalid values like '...' become NaN)
load['Relative_Sampling_Error'] = pd.to_numeric(load['Relative_Sampling_Error'], errors='coerce')

# Step 2: Optionally drop rows with missing Relative_Sampling_Error (if needed)
# You can also fill with mean or median instead, depending on your analysis needs
load = load.dropna(subset=['Relative_Sampling_Error'])


# Summary statistics, based on the file
print(load.describe())

# Correlation heatmap
plt.figure(figsize=(10, 6))
load['RD_Value'] = pd.to_numeric(load['RD_Value'], errors='coerce')
sns.heatmap(load.select_dtypes(include='number').corr(), annot=True, cmap='coolwarm')
plt.title('Correlation Heatmap')
plt.show()

# Histogram of RD_Value
# Clean RD_Value
load['RD_Value'] = pd.to_numeric(load['RD_Value'], errors='coerce')
load = load.dropna(subset=['RD_Value'])

# Now try heatmap again
sns.heatmap(load.select_dtypes(include='number').corr(), annot=True, cmap='coolwarm')


# Boxplot by Year
sns.boxplot(x='Year', y='RD_Value', data=load)
plt.xticks(rotation=45)
plt.title('RD Value by Year')
plt.show()

# Scatter plot of RD_Value vs Year
plt.figure(figsize=(10, 6))
sns.scatterplot(x='Year', y='RD_Value', data=load)
plt.title('RD Value over the Years')
plt.xlabel('Year')
plt.ylabel('RD Value')
plt.xticks(rotation=45)
plt.show()
