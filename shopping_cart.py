"""
Module: shopping_cart.py
Description: This module provides functionality to calculate and display 
             the total price of items in a shopping cart.
"""
def calculate_total(cart):
    """
    Calculate the total price of items in the shopping cart.

    :param cart: A list of dictionaries where each dictionary represents an item 
                with 'name' and 'price' keys.
    :return: The total price of all items in the cart.
    """
    total = 0
    for cart_item in cart:  # changed variable 'item' to 'cart_item' to avoid name conflict
        total += cart_item['price']
    return total

def display_total(total):
    """
    Display the total price of the items in the shopping cart.

    :param total: The total price to be displayed.
    """
    print("Total price: $" + str(total))

# updated product list with correct data type for prices
CART = [
    {'name': 'Item A', 'price': 10.99},
    {'name': 'Item B', 'price': 5.99},
    {'name': 'Item C', 'price': 8.49}  # ixed: replaced string with number
]

# displaying product information
for item in CART:
    print(f"Item: {item['name']} - Price: ${item['price']}")

# calculating the total amount and displaying it
shopping_cart_total = calculate_total(CART)
display_total(shopping_cart_total)
