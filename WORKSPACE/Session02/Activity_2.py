#######################################################################
# Activity 2 – Organising and Summarising
#
# What you're expected to do
# 1. Sort the list using both sorted() and sort(), explaining the difference.
# 2. Reverse the list and calculate min, max, and average.
# 3. Slice into quarters and identify which quarter performed best.
#######################################################################

import random
sales = [random.randint(10000, 30000) for _ in range(12)]

print("Unsorted sales data:", sales)
sales.sort()
print("Permanently sorted sales data:", sales)

sales.reverse()
print("Reversed sales data:", sales)
print("Min sales:", min(sales), "Max sales:", max(sales), "Average sales:", sum(sales)/len(sales))



