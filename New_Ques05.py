# 5️⃣ Correlation + Scatter Plot
# Select Feature1 and Feature6.
# Convert them into NumPy arrays.
# Calculate correlation coefficient using NumPy.
# Plot scatter plot.
# Display correlation value in title.
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv('Matplotlib/output.csv')
Feature01 = df['Feature1'].dropna()
Feature06 = df['Feature6'].dropna()
numpy_array01 = np.array(Feature01)
numpy_array06 = np.array(Feature06)
coref01 = np.corrcoef(numpy_array01)
coref06 = np.corrcoef(numpy_array06)
plt.scatter(coref01, numpy_array01)
plt.scatter(coref06, numpy_array06)
plt.title('Correlation Value')
plt.grid(True)
plt.show()