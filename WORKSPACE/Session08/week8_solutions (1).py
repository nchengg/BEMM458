# Week 8 – Files and Errors: Solutions

# Solution 1 — Reading From a File
try:
    with open("animals.txt") as file:
        animals_list = [line.strip() for line in file]
except FileNotFoundError:
    print("The file 'animals.txt' was not found.")
else:
    print("Number of animals:", len(animals_list))
    for animal in animals_list:
        print(animal.title())


# Solution 2 — Writing & Appending to a File
foods = []
for i in range(3):
    foods.append(input(f"Enter favourite food #{i+1}: "))

with open("favourites.txt", "w") as file:
    for food in foods:
        file.write(food + "\n")

extra = input("Enter one more favourite food: ")

with open("favourites.txt", "a") as file:
    file.write(extra + "\n")


# Solution 3 — ZeroDivisionError Handling
while True:
    first = input("Enter first number (or 'quit'): ")
    if first.lower() == "quit":
        break

    second = input("Enter second number: ")

    try:
        num1 = float(first)
        num2 = float(second)
        result = num1 / num2
    except ZeroDivisionError:
        print("You cannot divide by zero.")
    except ValueError:
        print("Please enter valid numbers.")
    else:
        print("Result:", result)


# Solution 4 — JSON Storage
import json

name = input("Enter your name: ")
data = {"username": name}

with open("user.json", "w") as file:
    file.write(json.dumps(data))

print("User saved.")


# Loading program
try:
    with open("user.json") as file:
        content = file.read()
except FileNotFoundError:
    pass
else:
    data = json.loads(content)
    print(f"Welcome back, {data['username']}!")


# Solution 5 — File Processing
valid_numbers = []

try:
    with open("numbers.txt") as file:
        for line in file:
            try:
                num = int(line.strip())
            except ValueError:
                continue
            else:
                valid_numbers.append(num)
except FileNotFoundError:
    print("numbers.txt not found.")
else:
    if valid_numbers:
        total = sum(valid_numbers)
        count = len(valid_numbers)
        average = total / count
        print("Valid numbers:", count)
        print("Sum:", total)
        print("Average:", average)
    else:
        print("No valid numbers found.")
