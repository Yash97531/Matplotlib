# 2️⃣ Statistical Analysis + Filtering + Plot
# Find mean and standard deviation of Feature6 using NumPy.
# Filter rows where Feature6 > mean.
# Count how many such rows exist.
# Plot a bar chart:
# Total rows
# Filtered rows

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv('Matplotlib/output.csv')
Feature6_mean = df['Feature6'].mean()
Feature6_std = df['Feature6'].std()
Filtered = df[df['Feature6']>Feature6_mean]
No_of_columns_left = Filtered.shape[0]
Total_rows = df.shape[0]
a = [Total_rows, No_of_columns_left]
plt.bar(a, color = 'red')
plt.show()
# print(Filtered)