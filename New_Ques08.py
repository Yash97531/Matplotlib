# 8️⃣ Mini Project Question (Full Analysis)
# Perform complete analysis:
# Handle missing values
# Remove duplicates

# Find:
# Most frequent category in Feature14
# Average of Feature6
# Maximum of Feature8

# Create:
# Create a subplot plot of the following graphs in one frame:
# Histogram of Feature6
# Pie chart of Feature14
# bar graph of Feature19 vs Average of Feature11
# Scatter plot of Feature1 vs Feature6
# Save all plots as images i am doing these questions 

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Cleaning the data:-
df = pd.read_csv('Matplotlib/output.csv')
df.dropna(axis = 0, inplace = True)
df.drop_duplicates(inplace = True)
df.reset_index(drop = True, inplace = True)

# Finding:-
a = df['Feature14'].value_counts().reset_index()
a.sort_values(by = 'count', ascending = False, inplace = True)
Most_frequent_caetogry = a.head(1)
Average_Feature06 = df['Feature6'].mean()
Maximum_Feature08 = df['Feature8'].max()

# Creating:-
plt.subplot(2, 2, 1)
plt.hist(df['Feature6'], bins = 5, color = 'purple', edgecolor = 'k', label = 'Feature06')
plt.legend(loc = 'upper right')
plt.xlabel('Values')
plt.ylabel('Index')
plt.title('Histogram of Feature 06')

plt.subplot(2, 2, 2)
plt.pie(a['count'], labels = a["Feature14"],autopct = '%1.1f%%',  colors = ['cyan', 'lightgreen', 'yellow'])
plt.legend(loc = 'upper left')
plt.title('Pie Chart of Feature 14')

plt.subplot(2, 2, 3)
grp = df.groupby('Feature19')['Feature11'].mean().reset_index()
plt.bar(grp['Feature19'], grp['Feature11'], color = 'red', edgecolor = 'k', width = 0.5, label = 'Feature 19 vs 11')
plt.legend(loc = 'upper right')
plt.xlabel('Feature 19')
plt.ylabel('Feature 11')
plt.title('Bar Graph of Feature 19 vs Feature 11')

plt.subplot(2, 2, 4)
plt.scatter(df['Feature1'], df['Feature6'], color = 'orange', label = 'Feature 01')
plt.legend(loc = 'upper right')
plt.grid(True)
plt.xlabel('Feature 01')
plt.ylabel('Feature 06')
plt.title('Scatter plot of Feature 01 vs Feature 06')
plt.tight_layout()
plt.savefig("analysis_plots.png")
plt.show()