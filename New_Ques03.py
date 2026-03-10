# 3️⃣ Grouping + Aggregation + Bar Graph
# Group data by Feature14.
# Find average of Feature1 for each category.
# Convert result into NumPy array.
# Plot a bar chart showing category vs average Feature1.
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
df = pd.read_csv('Matplotlib/output.csv')
a = df.groupby('Feature14')['Feature1'].mean().reset_index()
l = a['Feature1'].tolist()
numpy_array = np.array(l)
caetogry = a['Feature14']
plt.bar(caetogry, numpy_array, color = 'cyan', label = 'Feature01', edgecolor = 'k')
plt.legend(loc = 'upper right')
plt.xlabel('Caetogries')
plt.ylabel('Average of Feature 01')
plt.title('Caetogry vs Average Feature 01')
plt.tight_layout()
plt.show()