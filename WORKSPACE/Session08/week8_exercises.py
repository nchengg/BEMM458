# Week 8 – Files and Errors: Exercises

import json
from pathlib import Path

# Exercise 1 — Reading From a File
# --------------------------------
# You are given a text file called animals.txt containing one animal name per line.
# Tasks:
# 1. Read all lines into a list, stripping whitespace.
# 2. Print the total number of animals.
# 3. Print each animal in title case.
# 4. Handle FileNotFoundError with a friendly message.
def read_animals():
    """Reads animals from animals.txt and prints them."""
    file_path = Path('animals.txt')
    try:
        # read_text().splitlines() is a concise way to get all lines
        animals = file_path.read_text().splitlines()
        print(f"Total number of animals: {len(animals)}")
        for animal in animals:
            print(animal.title())
    except FileNotFoundError:
        print(f"Sorry, the file {file_path} does not exist.")

# Exercise 2 — Writing & Appending to a File
# -------------------------------------------
# 1. Ask the user for three favourite foods.
# 2. Write them to favourites.txt (one per line).
# 3. Ask for one additional food and append it to the file.
def manage_favourites():
    """Writes and appends user's favourite foods to a file."""
    favourites_file = Path('favourites.txt')
    
    # Collect 3 foods and write them to the file
    foods = []
    for _ in range(3):
        food = input("Enter a favourite food: ")
        foods.append(food)
    
    # The '\n'.join() method is an efficient way to write multiple lines
    favourites_file.write_text('\n'.join(foods) + '\n')
    print(f"Wrote {len(foods)} foods to {favourites_file}.")

    # Ask for one more and append it
    additional_food = input("Enter one more favourite food to append: ")
    with favourites_file.open(mode='a') as file:
        file.write(additional_food + '\n')
    print(f"Appended {additional_food} to {favourites_file}.")

# Exercise 3 — Handling ZeroDivisionError
# ---------------------------------------
# 1. Ask the user for two numbers.
# 2. Attempt to divide them using try-except.
# 3. Handle ZeroDivisionError and ValueError.
# 4. Use an else block to print result.
# 5. Repeat until the user types 'quit'.
def safe_division():
    """Performs division, handling potential user errors."""
    while True:
        first_input = input("Enter the first number (or 'quit' to exit): ")
        if first_input.lower() == 'quit':
            break
        
        second_input = input("Enter the second number: ")

        try:
            x = float(first_input)
            y = float(second_input)
            result = x / y
        except ValueError:
            print("Error: Please enter valid numbers.")
        except ZeroDivisionError:
            print("Error: Cannot divide by zero.")
        else:
            print(f"The result of {x} / {y} is: {result}")

# Exercise 4 — JSON Storage
# -------------------------
# 1. Ask the user for their name.
# 2. Store it in a dictionary and save to user.json using json.dump().
# 3. Write another program to read user.json and welcome the user.
# 4. Output fail message if user.json does not exist.
def store_user_name():
    """Asks for a user's name and stores it in a JSON file."""
    user_file = Path('user.json')
    name = input("Enter your name: ")
    user_data = {'name': name}
    
    # Use write_text with json.dumps for a clean one-liner
    user_file.write_text(json.dumps(user_data, indent=4))
    print(f"Your name has been stored in {user_file}.")

def greet_user():
    """Reads the user's name from a JSON file and prints a greeting."""
    user_file = Path('user.json')
    try:
        user_data = json.loads(user_file.read_text())
        name = user_data.get('name', 'there') # .get() is safer than direct access
        print(f"Welcome back, {name}!")
    except FileNotFoundError:
        print(f"Error: The file {user_file} was not found.")
    except json.JSONDecodeError:
        print(f"Error: The file {user_file} does not contain valid JSON.")

# Exercise 5 — File Processing With Error Handling
# ------------------------------------------------
# Given numbers.txt containing one number per line (some invalid):
# 1. Read file line by line.
# 2. Convert to int inside try-except.
# 3. Store valid numbers.
# 4. Ignore invalid lines silently.
# 5. Print count, sum, and average of valid numbers.
def process_numbers():
    """Reads and analyzes numbers from numbers.txt, handling errors."""
    numbers_file = Path('numbers.txt')
    valid_numbers = []

    try:
        lines = numbers_file.read_text().splitlines()
        for line in lines:
            try:
                # Strip whitespace just in case
                number = int(line.strip())
                valid_numbers.append(number)
            except ValueError:
                # This will silently ignore lines that aren't valid integers
                pass 
    
        if valid_numbers:
            total = sum(valid_numbers)
            average = total / len(valid_numbers)
            print(f"Count of valid numbers: {len(valid_numbers)}")
            print(f"Sum of valid numbers: {total}")
            print(f"Average of valid numbers: {average:.2f}")
        else:
            print("No valid numbers found in the file.")
            
    except FileNotFoundError:
        print(f"Error: The file {numbers_file} does not exist.")

# --- Main execution block to run the functions ---
if __name__ == "__main__":
    print("--- Running Exercise 1 ---")
    read_animals()
    print("\n--- Running Exercise 2 ---")
    manage_favourites()
    print("\n--- Running Exercise 3 ---")
    # safe_division() # Uncomment to run interactive division loop
    print("\n--- Running Exercise 4 (Store & Greet) ---")
    store_user_name()
    greet_user()
    print("\n--- Running Exercise 5 ---")
    process_numbers()
