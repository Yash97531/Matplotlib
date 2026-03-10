# 6 New Column Creation + Visualization
# Create new column:
# "High" if Feature1 > mean
# "Low" otherwise
# Count High and Low values
# Plot bar chart.
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv('Matplotlib/output.csv')
df['High'] = ['High' if x > df['Feature1'].mean() else 'Low' for x in df['Feature1']]
a = df['High'].value_counts().reset_index()
arr = np.array(a['count'])
plt.bar(a.index, arr, width=0.4)
plt.title("High vs Low Count")
plt.xlabel("Category")
plt.ylabel("Count")
plt.tight_layout()
plt.show()