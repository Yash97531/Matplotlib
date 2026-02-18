import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv('Matplotlib/company_sales_data.csv')
profit = df ['total_profit'].tolist()
month = df['month_number'].tolist()
plt.plot(month, profit, color = 'cyan', label = 'Total sales of data last year')
plt.title('company profit per month')
plt.xlabel('Month number')
plt.ylabel('Total Profit')
plt.xticks(month)
plt.yticks([100000, 200000, 300000, 400000, 500000])
plt.show()
