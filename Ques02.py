# Exercise 2: Get total profit of all months and show line plot with the following Style properties
# Generated line plot must include following Style properties: –

# Line Style dotted and Line-color should be red
# Show legend at the lower right location.
# X label name = Month Number
# Y label name = Sold units number
# Add a circle marker.
# Line marker color as read
# Line width should be 3

import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv('Matplotlib/company_sales_data.csv')
Total_profit = df['total_profit'].tolist()
month = df['month_number'].tolist()
plt.plot(month, Total_profit, label = 'Profit data of last year', color = 'red', marker = "o", linewidth = 3, linestyle = '--', markerfacecolor = 'k')
plt.xlabel('Month Number')
plt.ylabel('Sold Units Number')
plt.legend(loc = 'lower right')
plt.xticks(month)
plt.yticks([100000, 200000, 300000, 400000, 500000])
plt.title('Company sales data of last year')
plt.show()
# print(df)