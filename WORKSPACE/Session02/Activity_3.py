#######################################################################
# Activity 3 – Loops and Comprehensions
#
# What you're expected to do
# 1. Use a loop to calculate month-over-month growth rates (%).
# 2. Rewrite the same calculation as a list comprehension.
# 3. Filter out months with sales >= 20,000 using a comprehension.
#######################################################################

import random

sales = [random.randint(10000, 30000) for _ in range(12)]

growthRates = []

for i in range(1, len(sales)):
    growth = (sales[i] - sales[i-1]) / sales[i-1] * 100
    growthRates.append(round(growth, 2))
print("Growth rates (loop):", growthRates)

growthRatesComprehension = [round((sales[i] - sales[i-1]) / sales[i-1] * 100, 2) for i in range(1, len(sales))]
print("Growth rates (comprehension):", growthRatesComprehension)

highMonths = [i for i in sales if i >= 20000]
print("High months:", highMonths)