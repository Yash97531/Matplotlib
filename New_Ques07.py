# 7 Outlier Detection + Highlighting
# Use NumPy:
# mean ± 2 × std on Feature1
# Identify outliers.
# Plot scatter plot of all data.
# Highlight outliers in different color.

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('Matplotlib/output.csv')

a = df['Feature1'].mean() + 2 * df['Feature1'].std()
b = df['Feature1'].mean() - 2 * df['Feature1'].std()

c = df[(df['Feature1'] > a) | (df['Feature1'] < b)]
plt.scatter(df.index, df['Feature1'])
plt.scatter(c.index, c['Feature1'])

plt.title("Outlier Detection")
plt.show()
