#######################################################################
# Week 4 – Activity 1: If Statements & Lists
#
# What you're expected to do
# 1. Write an if–elif–else chain to apply a discount to a shopping cart
#    based on spend and membership status.
# 2. Use 'if' with lists to check for special items and handle an empty cart.
# 3. Print a clear receipt summary.
#
# Hints
# - Use >= for threshold checks.
# - Combine conditions with 'and'/'or'.
# - Check an empty list with: if not my_list:
#######################################################################

# 1) Discount rules (complete the TODOs):
# - If spend >= 200 and member is True -> 20% discount
# - Elif spend >= 200 and member is False -> 10% discount
# - Elif spend between 100 and 199 (inclusive) -> 5% discount
# - Else -> 0%

spend = 185
member = True  # change to False to test non-members

if spend >= 200 and member:
    discount_pct = 0.20
elif spend >= 200 and not member:
    discount_pct = 0.10
elif 100 <= spend <= 199:
    discount_pct = 0.05
else:
    discount_pct = 0.00

discount_value = round(spend * discount_pct, 2)
total_after = round(spend - discount_value, 2)

print(f"Spend: £{spend}, Member: {member}, Discount: {discount_pct*100:.0f}% -> Total: £{total_after}")  # OUTPUT:

# 2) 'if' with lists: flag special items and handle empty carts
cart = ["bread", "milk", "eggs", "gift-card"]  # try: cart = []
specials = ["gift-card", "alcohol"]
if not cart:
    print("Cart is empty.")  # OUTPUT:
else:
    for item in cart:
        if item in specials:
            print(f"{item} requires ID check or special handling.")  # OUTPUT:
        else:
            print(f"{item} added to basket.")  # OUTPUT:

# 3) Receipt summary
print("—"*40)
print(f"Items: {len(cart)} | Subtotal: £{spend} | Discount: £{discount_value} | Total: £{total_after}")  # OUTPUT:
