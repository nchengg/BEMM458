# Fitness-Style Example Questions

# Example 1 – Daily Water Intake
water_cups = [6, 7, 5, 8, 9, 10, 7]

# Tasks:
# 1. Create average_intake(data) returning the average.
# 2. Create above_target(data, target) returning count of days above target.
# 3. Store in water_utils.py.
# 4. Import and test the functions.

average_intake = sum(water_cups) / len(water_cups)
print("Average:", average_intake)

'''
def above_target(data, target):
    counter = 0
    for i in data:
        if i > target:
            counter = counter + 1
    return counter
'''
from water_utils import above_target

print("Days above target:", above_target(water_cups, 7))

# Example 2 – Heart Rate Measurements
heart_rates = [68, 72, 70, 65, 74, 71]

# Tasks:
# 1. Write min_rate(data) returning min heart rate.
# 2. Write range_rate(data) returning difference between max and min.
# 3. Store in hr_utils.py.
# 4. Import and test the functions.
'''
def min_rate(data):
    return min(data)

def range_rate(data):
    return max(data) - min(data)
'''
from hr_utils import min_rate, range_rate

print("Min heart rate:", min_rate(heart_rates))
print("Heart rate range:", range_rate(heart_rates))

