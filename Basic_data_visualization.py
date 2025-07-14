import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load your cleaned data
load = pd.read_csv('research-and-development-survey-2024.csv')

# Bar plot: Average RD_Value per Year: as their the only numerals
plt.figure(figsize=(10,6))
sns.barplot(x='Year', y='RD_Value', data=load, estimator='mean', ci=None)
plt.title('Average RD Value per Year')
plt.ylabel('Average RD Value')
plt.xticks(rotation=45)
plt.show()

# Line plot: Total RD_Value per Year
yearly_rd = load.groupby('Year')['RD_Value'].sum().reset_index()

plt.figure(figsize=(10,6))
sns.lineplot(x='Year', y='RD_Value', data=yearly_rd, marker='o')
plt.title('Total RD Value Over Years')
plt.ylabel('Total RD Value')
plt.xticks(rotation=45)
plt.show()

