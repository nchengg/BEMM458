#######################################################################
# Activity 3 – Bar Chart of Quarterly Revenue
#
# What you're expected to do
# 1. Create two lists: quarters (Q1–Q4) and revenue numbers (£k).
# 2. Plot a bar chart (plt.bar).
# 3. Add a title, axis labels, and show values above each bar.
# Stretch: Try horizontal bars with plt.barh.
#######################################################################

import matplotlib.pyplot as plt

quarters = ["Q1", "Q2", "Q3", "Q4"]
revenue = [120, 150, 170, 160]

# 1) Bar chart
bars = plt.bar(quarters, revenue)

# 2) Add YOUR labels
plt.title("____")
plt.xlabel("____")
plt.ylabel("____")

# 3) Show values
for bar in bars:
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, height + 2, f"{height}", ha="center")

plt.show()

# Stretch: horizontal bar chart (uncomment)
# plt.barh(quarters, revenue)
# plt.title("____")
# plt.xlabel("____")
# plt.ylabel("____")
# plt.show()
