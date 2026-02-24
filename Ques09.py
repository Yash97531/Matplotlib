# Exercise Question 10: 
# Read all product sales data and show it using the stack plot
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
plt.stackplot(month, face_cream, face_wash, tooth_paste, bathing_soap, shampoo, moisturizer, colors=['m','c','r','k','g','y'], labels=['face_cream', 'face_wash', 'tooth_paste', 'bathing_soap', 'shampoo', 'moisturizer'])
plt.title('All product sales data using stack plot')
plt.xlabel('Month Number')
plt.ylabel('Sales units in number')
plt.legend(loc = 'upper left')
plt.show()