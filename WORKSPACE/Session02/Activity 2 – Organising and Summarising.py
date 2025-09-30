#######################################################################
# Activity 2 – Organising and Summarising
#
# What you're expected to do
# 1. Sort the list using both sorted() and sort(), explaining the difference.
# 2. Reverse the list and calculate min, max, and average.
# 3. Slice into quarters and identify which quarter performed best.
#######################################################################

sales = [12000, 15000, 17000, 16000, 18000, 17500, 21000, 20500, 22000, 21500, 23000, 24000]

# 1) Sort
print("Temporary sort:", sorted(sales))  # OUTPUT:
sales.sort()
print("Permanent sort:", sales)  # OUTPUT:

# 2) Reverse + stats
sales.reverse()
print("Reversed:", sales)  # OUTPUT:
print("Min:", min(sales), "Max:", max(sales), "Average:", sum(sales)/len(sales))  # OUTPUT:

# 3) Slices and best quarter
q_totals = [sum(sales[i:i+3]) for i in range(0, 12, 3)]
print("Quarter totals:", q_totals, "Best Q:", q_totals.index(max(q_totals))+1)  # OUTPUT:
