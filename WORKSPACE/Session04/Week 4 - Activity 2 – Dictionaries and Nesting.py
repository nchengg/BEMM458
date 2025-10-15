#######################################################################
# Week 4 – Activity 2: Dictionaries & Nesting
#
# What you're expected to do
# 1. Create and modify a product dictionary (add, update, and access).
# 2. Use dict.get() with a default when a key might be missing.
# 3. Create a nested structure: customers with a list of orders each,
#    then loop through keys/values to print a readable report.
#######################################################################

# 1) Basic product dictionary
product = {
    "sku": "SKU-101",
    "name": "Wireless Mouse",
    "price": 24.99,
    "stock": 120
}

# Update price and stock
product["price"] = 22.99
product["stock"] -= 5
# Add a new key
product["category"] = "Peripherals"

print("Product record:", product)  # OUTPUT:

# 2) dict.get() with default
colour = product.get("colour", "N/A")
print("Colour:", colour)  # OUTPUT:

# 3) Nesting: customers and their orders
customers = {
    "Aisha": {"email": "aisha@example.com", "orders": ["SKU-101", "SKU-202"]},
    "Ben":   {"email": "ben@example.com",   "orders": ["SKU-303"]},
    "Chen":  {"email": "chen@example.com",  "orders": []},
}

# Loop through keys, values, and items
for name, info in customers.items():
    email = info.get("email", "unknown")
    orders = info.get("orders", [])
    print(f"Customer: {name} | Email: {email} | Orders count: {len(orders)}")  # OUTPUT:
    # Print each order SKU (if any)
    if orders:
        for sku in orders:
            print(" -", sku)  # OUTPUT:
    else:
        print(" - No orders yet")  # OUTPUT:
