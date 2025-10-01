#######################################################################
# Activity 1 – Lists in Action
#
# What you're expected to do
# 1. Create a list of monthly sales and access specific elements using indexing.
# 2. Modify values (update, append, insert, remove) and explain in comments
#    why you would use each method.
# 3. Slice the list into quarters and compare Q1 vs Q2 totals.
#######################################################################

import random

sales = [random.randint(10000, 25000) for _ in range(12)]
print("First month:", sales[0], "Last month:", sales[-1])
for i in range(len(sales)):
    print(f"Month {i+1} sales: {sales[i]}")


valueAction = input("Type 'a' to append, 'i' to insert at start, 'u' to update, 'r' to remove: ").strip().lower()

if valueAction == 'a':
    sales.append(int(input("Enter a sales value to add: ")))
    print("Sales after appending:", sales)
elif valueAction == 'i':
    sales.insert(0, int(input("Enter a sales value to insert at start: ")))
    print("Sales after inserting at start:", sales)
elif valueAction == 'u':
    indexToUpdate = int(input("Enter the month index to update (0-11): "))
    if 0 <= indexToUpdate < len(sales):
        sales[indexToUpdate] = int(input("Enter the new sales value: "))
        print("Sales after updating month", indexToUpdate + 1, ":", sales)
    else:
        print("Invalid month index.")
elif valueAction == 'r':
    indexToRemove = int(input("Enter the month index to remove (0-11): "))
    if 0 <= indexToRemove < len(sales):
        sales.pop(indexToRemove)
        print("Sales after removing month", indexToRemove + 1, ":", sales)
    else:
        print("Invalid month index.")
else:
    print("Invalid action.")

q1 = sales[:3]
q2 = sales[3:6]
q3 = sales[6:9]
q4 = sales[9:12]
print("Q1 total:", sum(q1), "Q2 total:", sum(q2), "Q3 total:", sum(q3), "Q4 total:", sum(q4))
if sum(q1) > sum(q2):
    print("Q1 performed better than Q2")
elif sum(q1) < sum(q2):
    print("Q2 performed better than Q1")
else:
    print("Q1 and Q2 performed equally")
print("Q3 total:", sum(q3), "Q4 total:", sum(q4))

if sum(q3) > sum(q4):
    print("Q3 performed better than Q4")
elif sum(q3) < sum(q4):
    print("Q4 performed better than Q3")
if sum(q1) > sum(q3):
    print("Q1 performed better than Q3")
elif sum(q1) < sum(q3):
    print("Q3 performed better than Q1")
if sum(q2) > sum(q4):
    print("Q2 performed better than Q4")
elif sum(q2) < sum(q4):
    print("Q4 performed better than Q2")
if sum(q1) > sum(q4):
    print("Q1 performed better than Q4")
elif sum(q1) < sum(q4):
    print("Q4 performed better than Q1")
if sum(q2) > sum(q3):
    print("Q2 performed better than Q3")
elif sum(q2) < sum(q3):
    print("Q3 performed better than Q2")
if sum(q3) > sum(q4):
    print("Q3 performed better than Q4")
elif sum(q3) < sum(q4):
    print("Q4 performed better than Q3")
