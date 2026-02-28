# 1️⃣ Data Cleaning + Visualization
# Load the dataset.
# Find total missing values in each column.
# Replace missing values in numeric columns using column mean (NumPy).
# Remove rows where Feature4 is missing.
# Plot a histogram of Feature1.

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
df = pd.read_csv('Matplotlib/output.csv')
df['Feature1'] = df['Feature1'].fillna(df['Feature1'].mean())
df['Feature2'] = df['Feature2'].fillna(df['Feature2'].mean())
df['Feature3'] = df['Feature3'].fillna(df['Feature3'].mean())
df['Feature5'] = df['Feature5'].fillna(df['Feature5'].mean())
df['Feature6'] = df['Feature6'].fillna(df['Feature6'].mean())
df['Feature7'] = df['Feature7'].fillna(df['Feature7'].mean())
df['Feature8'] = df['Feature8'].fillna(df['Feature8'].mean())
df['Feature9'] = df['Feature9'].fillna(df['Feature9'].mean())
df['Feature10'] = df['Feature10'].fillna(df['Feature10'].mean())
df['Feature11'] = df['Feature11'].fillna(df['Feature11'].mean())
df['Feature13'] = df['Feature13'].fillna(df['Feature13'].mean())
df['Feature16'] = df['Feature16'].fillna(df['Feature16'].mean())
df['Feature17'] = df['Feature17'].fillna(df['Feature17'].mean())
df.dropna(subset=['Feature4'], inplace = True)
print(df.isnull().sum())
plt.hist(df['Feature1'] , bins = 5, color = 'cyan', edgecolor = 'black')
plt.xlabel('Feature1')
plt.show()
