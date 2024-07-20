# Question 3

# Task 1

def print_order_details(orders):
    for order in orders:
        # Unpack the tuple
        customer_name, product, quantity = order

        # Format and print the order details
        print(f"Customer: {customer_name}\nProduct: {product}\nQuantity: {quantity}\n")

# Sample data
orders = [
    ("Alice", "Laptop", 1),
    ("Bob", "Camera", 2),
    # More orders...
]

# Call the function with the sample data
print_order_details(orders)