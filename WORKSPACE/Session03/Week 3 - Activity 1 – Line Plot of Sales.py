#######################################################################
# Activity 1 – Line Plot of Sales
#
# What you're expected to do
# 1. Create a simple list of monthly sales numbers.
# 2. Plot them using a line graph (plt.plot).
# 3. Add a title, axis labels, and grid.
# Stretch: Add a second line for last year’s sales and use a legend.
#######################################################################

import matplotlib.pyplot as plt

# Monthly sales (£k)
sales_2024 = [50, 55, 60, 58, 62, 65, 70, 68, 72, 75, 78, 80]
months = ["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"]

# 1) Line plot
plt.plot(months, sales_2024, marker="o")

# 2) Add YOUR title and axis labels below
plt.title("____")
plt.xlabel("____")
plt.ylabel("____")

plt.grid(True)
plt.show()

# Stretch: Add comparison line (uncomment and complete)
# sales_2023 = [45, 48, 55, 53, 57, 60, 65, 63, 67, 70, 72, 75]
# plt.plot(months, sales_2024, marker="o", label="2024")
# plt.plot(months, sales_2023, marker="s", label="2023")
# plt.title("____")
# plt.xlabel("____")
# plt.ylabel("____")
# plt.legend()
# plt.grid(True)
# plt.show()
