# 4️⃣ Categorical Analysis + Pie Chart
# Count how many "Yes" and other values are in Feature18.
# Convert counts into NumPy array.
# Plot a pie chart showing percentage distribution.
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
df = pd.read_csv('Matplotlib/output.csv')
a = df['Feature18'].value_counts().reset_index()
numpy_array = np.array(a['count'])
# print(numpy_array)
l = a['Feature18']
plt.pie(numpy_array, labels= l,autopct = '%1.1f%%' ,colors=['skyblue', 'coral'])
plt.legend(loc = 'upper right')
plt.title('Yes vs No graph')
plt.show()