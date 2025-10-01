#######################################################################
# Activity 2 – Scatter Plot of Marketing Spend vs Customers
#
# What you're expected to do
# 1. Create two lists: weekly marketing spend (£k) and new customers.
# 2. Plot a scatter chart (plt.scatter).
# 3. Add a title and axis labels.
# Stretch: Change colour and size of points to make the plot more informative.
#######################################################################

import matplotlib.pyplot as plt

spend = [5, 6, 7, 8, 9, 10, 11, 12]
customers = [50, 55, 65, 70, 80, 85, 95, 100]

# 1) Basic scatter
plt.scatter(spend, customers)

# 2) Add YOUR labels
plt.title("____")
plt.xlabel("____")
plt.ylabel("____")

plt.grid(True)
plt.show()

# Stretch: custom size/colour (uncomment and complete)
# sizes = [s*10 for s in spend]
# plt.scatter(spend, customers, s=sizes, c=customers, cmap="viridis")
# plt.title("____")
# plt.xlabel("____")
# plt.ylabel("____")
# plt.colorbar(label="New Customers")
# plt.grid(True)
# plt.show()
