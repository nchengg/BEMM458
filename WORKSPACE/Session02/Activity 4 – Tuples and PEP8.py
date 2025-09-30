#######################################################################
# Activity 4 – Tuples and PEP8
#
# What you're expected to do
# 1. Create a product tuple and demonstrate immutability.
# 2. Create a catalogue (list of tuples) and print a formatted report.
# 3. Write a function to apply a discount to a price, following PEP8 style.
#######################################################################

# 1) Product tuple
product = ("Laptop Pro 14", 1299.99, "SKU-LTP14")
print("Product tuple:", product)  # OUTPUT:
# Try mutation (should fail if uncommented): product[0] = "Desktop"

# 2) Catalogue
catalogue = [
    ("Mouse", 24.99, "SKU-MSE01"),
    ("Keyboard", 79.99, "SKU-KBD02"),
    ("Monitor", 219.99, "SKU-MON03"),
]
for name, price, sku in catalogue:
    print(f"{name:10} | £{price:7.2f} | {sku}")  # OUTPUT:

# 3) Function (PEP8)
def compute_discounted_price(price, discount_pct):
    """Return price after applying discount_pct (0–100)."""
    if discount_pct < 0 or discount_pct > 100:
        raise ValueError("discount_pct must be between 0 and 100.")
    return round(price * (1 - discount_pct / 100), 2)

print("Discounted:", compute_discounted_price(100, 15))  # OUTPUT:
