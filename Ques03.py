# Exercise 3: Read all product sales data and show it  using a multiline plot
# Display the number of units sold per month for each product using multiline plots. (i.e., Separate Plotline for each product ).

import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv('Matplotlib/company_sales_data.csv')
face_cream = df['facecream'].tolist()
face_wash = df['facewash'].tolist()
tooth_paste = df['toothpaste'].tolist()
bathing_soap = df['bathingsoap'].tolist()
shampoo = df['shampoo'].tolist()
moisturizer = df['moisturizer'].tolist()
month = df['month_number'].tolist()
plt.plot(month, face_cream, color = "blue", marker = 'o', markerfacecolor = 'blue', label = 'Face cream Sales Data')
plt.plot(month, face_wash, color = 'orange', marker = 'o', markerfacecolor = 'orange', label = 'Face wash Sales Data')
plt.plot(month, tooth_paste, color = 'green', marker = 'o', markerfacecolor = 'green', label = 'Tooth paste Sales Data')
plt.plot(month, bathing_soap, color = 'red', marker = 'o', markerfacecolor = 'red', label = 'bathing soap Sales Data')
plt.plot(month, shampoo, color = 'magenta', marker = 'o', markerfacecolor = 'magenta', label = 'shampoo Sales Data')
plt.plot(month, moisturizer, color = 'brown', marker = 'o', markerfacecolor = 'brown', label = 'moisturizer Sales Data')
plt.xticks(month)
plt.yticks([1000, 2000, 4000, 6000, 8000, 10000, 12000, 15000, 18000])
plt.legend(loc = 'upper left')
plt.xlabel('Month number')
plt.ylabel('Sales units in number')
plt.title('Sales Data')
plt.show() 
