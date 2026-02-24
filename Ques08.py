# Exercise 9: 
# Read Bathing soap , facewash of all months and display it using the Subplot
import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("Matplotlib/company_sales_data.csv")
bathing_soap = df['bathingsoap'].tolist()
month = df['month_number'].tolist()
plt.subplot(2, 1, 1)
plt.plot(month, bathing_soap, color = 'black', marker = 'o', markerfacecolor = 'k', linewidth = 3)
plt.title('Sales data of a bathing soap')
plt.xticks(month)
plt.yticks([7500, 10000, 12500])
facewash = df['facewash'].tolist()
plt.subplot(2, 1, 2)
plt.plot(month, facewash, color = 'red', marker = 'o', markerfacecolor = 'r', linewidth = 3)
plt.xticks(month)
plt.yticks([1500, 2000])
plt.title('Sales data of a facewash')
plt.ylabel('Sales units in number')
plt.xlabel('Month Number')
plt.tight_layout()
plt.show()