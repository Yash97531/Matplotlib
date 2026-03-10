# 6️⃣ Top Values + Line Chart
# Sort dataset by Feature8 in descending order.
# Select top 15 rows.
# Convert Feature8 to NumPy array.
# Plot line chart of top 15 values.
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv('Matplotlib/output.csv')
Feature08 = df['Feature8'].dropna()
a = Feature08.sort_values(ascending=False)
top15 = a.head(15)
numpy_array = np.array(top15)
plt.plot()
print(top15)