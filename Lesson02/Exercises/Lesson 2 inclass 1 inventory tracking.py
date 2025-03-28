# In-class Exercise 1: Inventory Management System
# =============================

# Step 1: Create a dictionary where the keys are product names and the values are dictionaries containing price and stock quantity
inventory = {
    "apple": {"price": 0.5, "stock": 100},
    "banana": {"price": 0.3, "stock": 150},
    "orange": {"price": 0.7, "stock": 80},
    "coffee": {"price": 0.6, "stock": 120},
    "green tea": {"price": 0.3, "stock": 150},
    "rooibos": {"price": 0.7, "stock": 80}
}

# Step 2: Add a new product to the inventory
inventory["grape"] = {"price": 1.0, "stock": 200}
inventory["pineapple"] = {"price": 1.8, "stock": 100}

# Step 3: Update the stock of a product when an item is sold with proper validation
def sell_product(product_name, quantity):
    # Validate quantity
    if quantity <= 0:
        print(f"Error: Quantity must be a positive integer for '{product_name}'.")
        return
    
    # Check if the product exists in the inventory
    if product_name not in inventory:
        return f"Error: Product '{product_name}' not found in inventory."
        
    
    # Check if there is enough stock
    if inventory[product_name]["stock"] < quantity:
        return f"Error: Insufficient stock for '{product_name}'. Available: {inventory[product_name]['stock']}."
        
    
    # Update the stock
    inventory[product_name]["stock"] -= quantity
    return f"Sold {quantity} units of '{product_name}'. Remaining stock: {inventory[product_name]['stock']}."

# Step 4: Display the available products with formatted prices and stock
def display_inventory():
    print("Current Inventory:")
    print("{:<10} | {:<8} | {}".format("Product", "Price", "Stock"))
    print("-" * 30)
    for product, details in inventory.items():
        print(f"{product:<10} | ${details['price']:<7.2f} | {details['stock']}")

# Example usage

sell_product("apple", 3)          # Valid sale
sell_product("banana", 200)       # Should show insufficient stock
sell_product("pear", 5)           # Should show product not found
print (sell_product("orange", -2))        # Should show invalid quantity

# Display the updated inventory
display_inventory()