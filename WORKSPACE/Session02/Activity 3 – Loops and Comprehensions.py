#######################################################################
# Activity 3 – Loops and Comprehensions
#
# What you're expected to do
# 1. Use a loop to calculate month-over-month growth rates (%).
# 2. Rewrite the same calculation as a list comprehension.
# 3. Filter out months with sales >= 20,000 using a comprehension.
#######################################################################

sales = [12000, 15000, 17000, 16000, 18000, 17500, 21000, 20500, 22000, 21500, 23000, 24000]

# 1) Loop
growth_rates = []
for i in range(1, len(sales)):
    growth = (sales[i] - sales[i-1]) / sales[i-1] * 100
    growth_rates.append(round(growth, 2))
print("Growth rates (loop):", growth_rates)  # OUTPUT:

# 2) Comprehension
growth_rates_comp = [round((sales[i] - sales[i-1]) / sales[i-1] * 100, 2) for i in range(1, len(sales))]
print("Growth rates (comprehension):", growth_rates_comp)  # OUTPUT:

# 3) Filter >= 20k
high_months = [s for s in sales if s >= 20000]
print("High months:", high_months)  # OUTPUT:
