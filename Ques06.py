# Exercise 6: 
# Read sales data of bathing soap of all months and show it using a bar chart
import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv('Matplotlib/company_sales_data.csv')
month = df['month_number'].tolist()
bathing_soap = df['bathingsoap'].tolist()
plt.bar(month, bathing_soap)
plt.title('bathingsoap sales data')
plt.xlabel('Month number')
plt.ylabel('Sold units in number')
plt.xticks(month)
plt.grid(True, linestyle = '--', linewidth = 1)
plt.show()