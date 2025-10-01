#######################################################################
# Activity 4 – Tuples and PEP8
#
# What you're expected to do
# 1. Create a product tuple and demonstrate immutability.
# 2. Create a catalogue (list of tuples) and print a formatted report.
# 3. Write a function to apply a discount to a price, following PEP8 style.
#######################################################################

import random

product = ("Laptop Pro 14", random.uniform(1000, 2000), "SKU-LTP14")
print("Product tuple:", product) 

# product[0] = "Desktop" # will raise an error

catalogue = [
    ("Mouse", random.uniform(10, 50), "SKU-MSE01"),
    ("Keyboard", random.uniform(20, 100), "SKU-KBD02"),
    ("Monitor", random.uniform(100, 300), "SKU-MON03"),
]
for name, price, sku in catalogue:
    print(f"{name:10} | £{price:7.2f} | {sku}")
