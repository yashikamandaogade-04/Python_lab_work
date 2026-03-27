"""
#lab assignment1
import pandas as pd
# Create DataFrame
data = {
    'carat': [0.23, 0.21, 0.23, 0.29, 0.31],
    'cut': ['Ideal', 'Premium', 'Good', 'Premium', 'Good'],
    'color': ['E', 'E', 'E', 'I', 'J'],
    'clarity': ['SI2', 'SI1', 'VS1', 'VS2', 'SI2'],
    'depth': [61.5, 59.8, 56.9, 62.4, 63.3],
    'table': [55.0, 61.0, 65.0, 58.0, 58.0],
    'price': [326, 326, 327, 334, 335],
    'x': [3.95, 3.89, 4.05, 4.20, 4.34],
    'y': [3.98, 3.84, 4.07, 4.23, 4.35],
    'z': [2.43, 2.31, 2.31, 2.63, 2.75]
}
df = pd.DataFrame(data)
# i) Mean price for each cut
print(df.groupby('cut')['price'].mean())
# ii) Count, min, max price for each cut
print(df.groupby('cut')['price'].agg(['count', 'min', 'max']))
# iii) Average x, y, z
print("Average x:", df['x'].mean())
print("Average y:", df['y'].mean())
print("Average z:", df['z'].mean())
"""
#lab assignment 2
import pandas as pd
# Load the dataset
# Note: Ensure openpyxl is installed (pip install openpyxl) to read .xlsx files
try:
    df_emp = pd.read_excel('employee.xlsx')
except FileNotFoundError:
    print("Error: The file 'employee.xlsx' was not found.")
    # Creating dummy data for demonstration purposes if file is missing
    emp_data = {
        'Employee ID': [101, 102, 103, 104],
        'Employee Name': ['Alice', 'Bob', 'Charlie', 'David'],
        'Department': ['Automotive', 'IT', 'Automotive', 'Sales'],
        'Designation': ['Developer', 'Manager', 'Tester', 'Developer']
    }
    df_emp = pd.DataFrame(emp_data)
# a) Print list of employees working for "Automotive" domain
print("--- Employees in Automotive Department ---")
automotive = df_emp[df_emp['Department'] == 'Automotive']
print(automotive)
# b) Print details of an employee with employee ID given by an end user
try:
    search_id = int(input("\nEnter Employee ID to search: "))
    details = df_emp[df_emp['Employee ID'] == search_id]
    
    if not details.empty:
        print(f"Details for Employee ID {search_id}:")
        print(details)
    else:
        print("No employee found with that ID.")
except ValueError:
    print("Invalid input. Please enter a numerical ID.")
# d) Print the list of all the Developers of Infosys
print("\n--- List of Developers ---")
developers = df_emp[df_emp['Designation'] == 'Developer']
print(developers)