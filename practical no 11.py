"""
#lab assignment 1
import pandas as pd
import matplotlib.pyplot as plt
# Creating dummy data to represent 'company_sales_data.csv'
data = {
    'month_number': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],
    'facecream': [2500, 2630, 2140, 3400, 3600, 2760, 2980, 3700, 3540, 1990, 2340, 2900],
    'facewash': [1500, 1200, 1340, 1130, 1740, 1555, 1120, 1400, 1780, 1890, 2100, 1760],
    'toothpaste': [5200, 5100, 4550, 5870, 4560, 4890, 4780, 5860, 6100, 8300, 7300, 7400],
    'total_profit': [211000, 183300, 224700, 222700, 209600, 201400, 295500, 361400, 234000, 266700, 412800, 300200]
}
df = pd.DataFrame(data)
# a) Line Plot for Total Profit
plt.figure(figsize=(8, 4))
plt.plot(df['month_number'], df['total_profit'], marker='o', color='b', label='Total Profit')
plt.title('Total Profit per Month')
plt.xlabel('Month Number')
plt.ylabel('Profit')
plt.grid(True, linestyle='--')
plt.show()
# b) Multiline Plot for all product sales
plt.figure(figsize=(8, 4))
plt.plot(df['month_number'], df['facecream'], label='Face Cream', marker='o')
plt.plot(df['month_number'], df['facewash'], label='Face Wash', marker='o')
plt.plot(df['month_number'], df['toothpaste'], label='Toothpaste', marker='o')
plt.title('All Product Sales Data')
plt.xlabel('Month Number')
plt.ylabel('Sales units')
plt.legend()
plt.show()
# c) Bar Chart for Face Cream and Face Wash
plt.figure(figsize=(8, 4))
plt.bar(df['month_number'] - 0.2, df['facecream'], width=0.4, label='Face Cream', align='center')
plt.bar(df['month_number'] + 0.2, df['facewash'], width=0.4, label='Face Wash', align='center')
plt.title('Facewash and Facecream Sales Data')
plt.xlabel('Month Number')
plt.ylabel('Sales units')
plt.legend()
plt.show()
# d) Pie Chart for Total Sale Data per product
labels = ['FaceCream', 'FaceWash', 'ToothPaste']
sales_data = [df['facecream'].sum(), df['facewash'].sum(), df['toothpaste'].sum()]
plt.figure(figsize=(6, 6))
plt.pie(sales_data, labels=labels, autopct='%1.1f%%', startangle=140)
plt.title('Total Sales Data for Last Year')
plt.show()
"""
#lab assignment2
import pandas as pd
import matplotlib.pyplot as plt
# Creating dummy dataset for recruitment
recruit_data = {
    'Company': ['Microsoft', 'Google', 'Amazon', 'IBM', 'Deloitte', 'Capgemini', 'ATOS Origin', 'Amdocs'],
    'New_Recruitments': [1500, 1800, 2200, 1200, 900, 1100, 600, 850]
}
df_recruit = pd.DataFrame(recruit_data)
# a) Bar Chart
plt.figure(figsize=(10, 5))
plt.bar(df_recruit['Company'], df_recruit['New_Recruitments'], color='teal')
plt.title('New Recruitments by Company')
plt.xticks(rotation=45)
plt.show()
# b) Pie Chart & c) Customized Pie Chart
plt.figure(figsize=(7, 7))
explode = [0.1 if x == 'Google' else 0 for x in df_recruit['Company']] # Highlight Google
plt.pie(df_recruit['New_Recruitments'], labels=df_recruit['Company'], autopct='%1.1f%%', explode=explode, shadow=True)
plt.title('Distribution of New Recruitments')
plt.show()
# d) Doughnut Chart
plt.figure(figsize=(7, 7))
plt.pie(df_recruit['New_Recruitments'], labels=df_recruit['Company'], autopct='%1.1f%%', pctdistance=0.85)
# Draw center circle to make it a doughnut
centre_circle = plt.Circle((0,0), 0.70, fc='white')
fig = plt.gcf()
fig.gca().add_artist(centre_circle)
plt.title('Recruitment Doughnut Chart')
plt.show()
# Comparison between IBM & Amdocs
compare_df = df_recruit[df_recruit['Company'].isin(['IBM', 'Amdocs'])]
plt.figure(figsize=(6, 4))
plt.bar(compare_df['Company'], compare_df['New_Recruitments'], color=['blue', 'orange'])
plt.title('Comparison: IBM vs Amdocs Recruitments')
plt.ylabel('Number of Employees')
plt.show()