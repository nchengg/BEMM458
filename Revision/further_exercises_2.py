# Training-Style Example Questions

# Example 1 – Study Session Tracker
study_minutes = [45, 60, 30, 50, 40, 70, 65]

# Tasks:
# 1. Print the total number of study sessions.
# 2. Print the highest and lowest number of minutes studied.
# 3. Convert the minutes to hours in a new list.
# 4. Loop through and compare each session to a 50-minute target.

print(f"Total study sessions: {sum(study_minutes)}")
print(f"Highest study minutes: {max(study_minutes)}")
print(f"Lowest study minutes: {min(study_minutes)}")

study_hours = [minutes / 60 for minutes in study_minutes]
print(study_hours)

for i in study_minutes:
    if i > 50:
        print(f"{i} : Above target")
    elif i < 50:
        print(f"{i} : Below target")
    else:
        print(f"{i} : On target")

# Example 2 – Machine Efficiency Readings
efficiency = [82, 88, 75, 90, 85, 92, 80, 87]

# Tasks:
# 1. Print the number of readings.
# 2. Slice and print the middle four readings.
# 3. Loop to show change between readings.
# 4. Convert the list to a tuple and explain why tuples are useful.

for i in efficiency:
    print(f"Efficiency reading: {i}")

middle_readings = efficiency[2:6]
print(f"Middle four readings: {middle_readings}")

for i in range(1, len(efficiency)):
    change = efficiency[i] - efficiency[i-1]
    print(f"Change from reading {i-1} to {i}: {change}")

efficiency_tuple = tuple(efficiency)
print(efficiency_tuple) # Tuples are immutable, useful for storing fixed or historical data.