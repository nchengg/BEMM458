
# Question – Data Visualization: Energy Usage Analysis
# A research team is analysing monthly household energy consumption (in kWh).
#
# months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun",
#           "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
#
# energy_kwh = [320, 290, 310, 280, 260, 240,
#               230, 235, 250, 270, 295, 310]
#
# Tasks:
# 1. Create a bar chart showing energy usage per month.
# 2. Add axis labels and a title: "Monthly Household Energy Consumption (kWh)".
# 3. On the same figure, plot a line graph of the running average (mean up to each month).
# 4. Rotate the x-axis labels diagonally for readability.
# 5. Identify the month with the minimum energy usage and annotate it on the chart.
# 6. In 3–4 sentences, discuss:
#    - which plot type is better for long-term trends,
#    - and which is better for comparing individual months.

import matplotlib.pyplot as plt
import numpy as np



months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun",
        "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

energy_kwh = [320, 290, 310, 280, 260, 240,
            230, 235, 250, 270, 295, 310]

#1
plt.figure(figsize=(12, 6))
plt.bar(months, energy_kwh, color='skyblue', label='Monthly Energy Usage')

#2
plt.xlabel('Month')
plt.ylabel('Energy Consumption (kWh)')
plt.title('Monthly Household Energy Consumption (kWh)')

#3
running_average = np.cumsum(energy_kwh) / np.arange(1, len(energy_kwh) + 1)
plt.plot(months, running_average)

#4
plt.xticks(rotation=45)

#5
min_energy = min(energy_kwh)
min_month = months[energy_kwh.index(min_energy)]

plt.annotate(f'Min: {min_energy} kWh',)
