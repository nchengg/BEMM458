import matplotlib.pyplot as plt 
import numpy as np  

def rainfall2_average(data, window):
    """Simple rainfall average function using convolution."""
    return np.convolve(data, np.ones(window)/window, mode='valid')


plt.figure(figsize=(10,5))


months2 = ["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"]
rainfall2 = [78, 52, 60, 85, 70, 55, 40, 48, 66, 90, 120, 130]

cumulative = np.cumsum(rainfall2)
ra = rainfall2_average(rainfall2, 3)


plt.bar(months2, rainfall2, color = "teal", label = "Monthly Rainfall")
plt.plot(months2, cumulative, "gx:", label = "Cumulative Rainfall")
plt.plot(months2[2:], ra, "r*-", label="3-Month Average")
plt.xlabel("Months")
plt.ylabel("Rainfall in mm")
plt.ylim(0, 500)
plt.title("Monthly Rainfall")


min_month = months2[rainfall2.index(min(rainfall2))]
plt.annotate("Lowest Rainfall",
             xy=(min_month, min(rainfall2)),
             xytext=(min_month, min(rainfall2)+50),
             arrowprops=dict(arrowstyle="->"))

plt.legend()
plt.grid(axis='y', linestyle = '--',alpha=0.7)

plt.show()