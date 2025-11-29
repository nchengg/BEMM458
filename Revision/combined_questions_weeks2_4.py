# ==========================================================
# Combined Exercises – Weeks 2 & 4
# ==========================================================
# These exercises test your understanding of:
# - Lists, slicing, and list comprehensions
# - Loops and calculations
# - Dictionaries, conditionals, and user input
# ==========================================================


# ----------------------------------------------------------
# Question 1 – Data Structures: Student Attendance
# ----------------------------------------------------------
# You are analysing monthly attendance data (as a percentage)
# for a group of students in one academic year.
#
# monthly_attendance = [92, 88, 85, 90, 94, 89, 91, 93, 87, 95, 90, 92]
#
# 1. Write a list comprehension to convert percentages into decimal
#    form (e.g., 92 → 0.92).
# 2. Slice the list to extract attendance for the second term
#    (March–June).
# 3. Use a loop to calculate and print the change in attendance
#    from one month to the next. Store these in `attendance_changes`.
# 4. Convert the attendance list into a tuple and explain why tuples
#    might be used for storing confirmed historical records.
# 5. (Extension) Use a conditional to print whether the average
#    attendance across the year was above 90%.

monthly_attendance = [92, 88, 85, 90, 94, 89, 91, 93, 87, 95, 90, 92]

#1
def percentageToDecimal(monthly_attendance):
    print([x / 100 for x in monthly_attendance])
#2
def secondTermAttendance(monthly_attendance):
    print(monthly_attendance[2:6])
#3
def attendanceChanges(monthly_attendance):
    attendance_changes = []
    for i in range(1, len(monthly_attendance)):
        change = monthly_attendance[i] - monthly_attendance[i-1]
        attendance_changes.append(change)
    print(attendance_changes) 
#4
def attendanceTuple(monthly_attendance):
    attendanceTuple = tuple(monthly_attendance)
    print(attendanceTuple) # Tuples are immutable, as historical data should not be changed.
#5
def averageAttendanceCheck(monthly_attendance):
    averageAttendance = sum(monthly_attendance) / len(monthly_attendance)
    if averageAttendance > 90:
        print("Average attendance is above 90%")
    else:
        print("Average attendance is 90% or below")


# ----------------------------------------------------------
# Question 2 – Control Flow & Dictionaries: Fitness Tracker
# ----------------------------------------------------------
# You are designing a simple fitness tracking program that records
# users’ weekly step counts.
#
# weekly_steps = {
#     "Alice": [7800, 8450, 9100, 10000],
#     "Ben": [5600, 6000, 6200, 7000],
#     "Cara": [9800, 10200, 11000, 11500]
# }
#
# 1. Ask the user to input a name.
# 2. Check if that name exists in the dictionary.
# 3. If it exists:
#       - Use a loop to calculate the average weekly steps.
#       - Print the name and average step count.
#       - Use an if statement to print:
#           "Excellent!" if average ≥ 9000,
#           "Good effort!" if between 7000–8999,
#           or "Needs improvement." if below 7000.
# 4. If the name doesn’t exist, print "User not found."
# 5. (Extension) Use a while loop to allow repeated lookups
#    until the user types "quit".
#
# (Hint: You can use sum() and len() to calculate averages.)

#
def fitness_tracker():
    weekly_steps = {
        "Alice": [7800, 8450, 9100, 10000],
        "Ben": [5600, 6000, 6200, 7000],
        "Cara": [9800, 10200, 11000, 11500]
    }

    while True:
        name = input("Input a name (or type 'quit' to exit): ")
        if name.lower() == "quit":
            break

        if name in weekly_steps:
            steps = weekly_steps[name]
            average_steps = sum(steps) / len(steps)
            print(f"{name}'s average weekly steps: {average_steps:.2f}")
        
            if average_steps >= 9000:
                print("Excellent!")
            elif 7000 <= average_steps < 9000:
                print("Good effort!")
            else:
                print("Needs improvement.")
        else:
            print("User not found.")


if __name__ == "__main__":
    print("---- Question 1 ----")
    percentageToDecimal(monthly_attendance)
    secondTermAttendance(monthly_attendance)
    attendanceChanges(monthly_attendance)
    attendanceTuple(monthly_attendance)
    averageAttendanceCheck(monthly_attendance)
    print("---- Question 2 ----")
    fitness_tracker()