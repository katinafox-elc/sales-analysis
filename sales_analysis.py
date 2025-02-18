# Import the pandas library
import pandas as pd
from regex import F

# Task 1: Import sales_data.csv and customer_data.csv into Pandas DataFrames
## Hint: Use the pd.read_csv() function to read the CSV files into DataFrames.
## Replace 'sales_data.csv' and 'customer_data.csv' with the actual file paths if they are not in the same directory as your script.
sales_df = # your code here
customers_df = # your code here


# Task 2: Join the two DataFrames on the customer_id column
## Hint: Use the .merge() method on one of the DataFrames to join them based on the 'customer_id' column.
## Choose the type of join that is appropriate for the analysis (e.g., inner join, left join).




# Task 3: Calculate total sales for each customer
## Hint: Create a new column 'total_sales' by multiplying 'quantity' and 'unit_price'.
## Then, use the.groupby() method to group the data by 'customer_id' and calculate the sum of 'total_sales'.


# Task 4: Display the results
## Hint: Print the total_sales_by_customer Series or DataFrame to show the total sales for each customer.



# Task 5: Summary Statistics
## Find the most profitable product.
### Calculate profit per product by multiplying quantity, unit_price and summing by product_id
product_profits = #your code here

### Type your answer to the question as a string
most_profitable_product =  'your response here'


## Find the customer with the highest order total.
### Get highest order total by customer
highest_order_customer = #Your Code Here

### Get customer details for highest order customer
customer_details = #Your Code Here

### Store result as string
highest_order_customer_name = f"Customer {customer_details['customer_name'].values[0]} had the highest order total of ${highest_order_customer.values[0]}"

## Find the product with the most sales.
### Get total quantity sold for each product
product_sales = #Your Code Here

### Get the product with highest quantity sold
most_sold_product = #Your Code Here
most_sold_quantity = #Your Code Here

### Store result as string
most_sold_product_result = f"Product {most_sold_product} had the highest sales with {most_sold_quantity} units sold"

## Find the customer who has the most orders
### Get order count by customer
customer_order_count = #Your Code Here

### Get customer details for customer with most orders
most_orders_customer = #Your Code Here

### Store result as string
most_orders_customer_result = f"Customer {most_orders_customer['customer_name'].values[0]} placed the most orders with {customer_order_count.values[0]} orders"

# Print the results
print(most_profitable_product)
print(highest_order_customer_name)
print(most_sold_product_result)
print(most_orders_customer_result)
