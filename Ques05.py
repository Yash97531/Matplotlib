# Exercise 5: 
# Read face cream and facewash product sales data and show it using the bar chart
# The bar chart should display the number of units sold per month for each product. Add a separate bar for each product in the same chart.
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
df = pd.read_csv('Matplotlib/company_sales_data.csv')
face_cream = df['facecream'].tolist()
face_wash = df['facewash'].tolist()
month = df['month_number'].tolist()
width = 0.35
x = np.arange(len(month))
plt.bar(x - width / 2, face_cream, width, color = 'blue', label = "Face cream sales data")
plt.bar(x + width / 2, face_wash, width, color = 'orange', label = 'Face wash sales data')
plt.legend(loc = 'upper left')
plt.xlabel('Month NUmber')
plt.ylabel('Sales units in number')
plt.title('Facewash and Facecream sales data')
plt.xticks(x, month)
plt.yticks([0, 500, 1000, 1500, 2000, 2500, 3000, 3500])
plt.show()