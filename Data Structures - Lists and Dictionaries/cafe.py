# Define the menu items sold in the cafe
menu = ["black_coffee", "latte", "cappuccino", "mocha", "hot_chocolate", "expresso", "flat_white"]

# Define the stock quantity for each menu item
stock = {"black_coffee": 10,
         "latte": 10,
         "cappuccino": 15,
         "mocha": 5,
         "hot_chocolate": 5,
         "expresso": 10,
         "flat_white": 5,
         }

# Define the price for each menu item
price = {"black_coffee": 2.9,
         "latte": 3.5,
         "cappuccino": 3.5,
         "mocha": 3.9,
         "hot_chocolate": 3.5,
         "expresso": 2.9,
         "flat_white": 3.5,
         }

# Initialize the total stock value
total_stock_value = 0

# Loop through each menu item to calculate the total stock value
for item in menu:

    # Calculate the total value for the current item and add it to the total stock value
    total_item_value = stock[item] * price[item]
    total_stock_value += total_item_value


# for item in menu:
#     # Retrieve the stock quantity and price for the current item
#     stock_quantity = stock[item]
#     item_price = price[item]
#
#     # Calculate the total value for the current item and add it to the total stock value
#     total_item_value = stock_quantity * item_price
#     total_stock_value += total_item_value


# Print the total stock value
print("Total Stock Value:", total_stock_value)
