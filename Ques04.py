# Exercise 4: 
# Read toothpaste sales data of each month and show it using a scatter plot
# Also, add a grid in the plot. gridline style should “–“

import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv('Matplotlib/company_sales_data.csv')
sales_toothpaste = df['toothpaste'].tolist()
month = df['month_number'].tolist()
plt.scatter(month, sales_toothpaste, marker = 'o', label = 'toothpaste sales data', s = 100)
plt.grid(True, linestyle = '--')
plt.xlabel('Month Number')
plt.ylabel('Number of units sold')
plt.xticks(month)
plt.yticks([4500, 5000, 5500, 6000, 6500, 7000, 7500, 8000])
plt.legend(loc = 'upper left')
plt.title('Tooth paste sales data')
plt.show()