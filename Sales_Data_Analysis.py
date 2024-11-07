import pandas as pd  
from datetime import datetime
Data={'Order ID':[1001,1002,1003,1004,1005],
      'Date':['2023-1-5','2023-1-10','2023-2-15','2023-3-20','2023-3-25'],
      'Product':['Widget A','Widget B','Widget A','Widget C','Widget B'],
      'Quantity Sold':[10,5,15,8,7],
      'Price Per Unit':[20,30,20,50,30],
      'Region':['North','South','East','North','West']}

Sales=pd.DataFrame(Data)
Sales['Date']=pd.to_datetime(Sales['Date'])
#Create a csv file
Sales.to_csv("Sales_Data_Analysis.csv",index=False)
print("CSV File Created Successfully!")
print(Sales)

#Add Column Total Sales
print("Add New Column Total Sales")
Sales['Total Sales']=Sales['Quantity Sold']*Sales['Price Per Unit']
print(Sales)

#Check Total Sales
print("Total Sales = ",Sales['Total Sales'].sum())

#Average Sales for each region
average_sales=Sales.groupby('Region')['Total Sales'].mean()
print("Average Sales of each region in data = ",average_sales)

#check highest sales in which month
monthly_sales=Sales.groupby('Date')['Total Sales'].sum()
highest_sales_month=monthly_sales.idxmax()
highest_sales_amount=monthly_sales.max()

print("Highest sales month name: ",highest_sales_month)
print("Highest Sales amount : ",highest_sales_amount)

