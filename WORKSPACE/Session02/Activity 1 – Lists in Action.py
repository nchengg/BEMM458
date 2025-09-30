#######################################################################
# Activity 1 – Lists in Action
#
# What you're expected to do
# 1. Create a list of monthly sales and access specific elements using indexing.
# 2. Modify values (update, append, insert, remove) and explain in comments
#    why you would use each method.
# 3. Slice the list into quarters and compare Q1 vs Q2 totals.
#######################################################################

# 1) Define a list of monthly sales (Jan–Jun)
sales = [12000, 15000, 17000, 16000, 18000, 17500]
print("First month:", sales[0], "Last month:", sales[-1])  # OUTPUT:

# 2) Modify: correct March’s value, add July, and remove last entry
sales[2] = 16500
sales.append(19000)
removed = sales.pop()
print("Corrected + added + removed:", sales, "Removed:", removed)  # OUTPUT:

# 3) Slice quarters and compare totals
q1 = sales[:3]
q2 = sales[3:6]
print("Q1 total:", sum(q1), "Q2 total:", sum(q2))  # OUTPUT:
