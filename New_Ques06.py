# 5 Top Values + Line Chart
# Sort dataset by Feature8 in descending order.
# Select top 15 rows.
# Convert Feature8 to NumPy array.
# Plot line chart of top 15 values.
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv('Matplotlib/output.csv')
Feature08 = df['Feature8'].dropna()
a = Feature08.sort_values(ascending=False).head(15)
numpy_array = np.array(a)
plt.plot(numpy_array, marker = 'o', )
plt.title("Top 15 Values of Feature8")
plt.xlabel("Index")
plt.ylabel("Feature8 Value")
plt.grid(True)

plt.show()