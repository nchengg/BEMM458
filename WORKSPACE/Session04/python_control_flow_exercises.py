# ==========================================
# Week 4: Control Flow and User Input
# ==========================================
# Save this file as exercises4.py
# Topics:
#   * if Statements and Boolean expressions
#   * Dictionaries
#   * Nesting
#   * User Input
#   * while Loops
# Learning Objectives:
#   * Write programs that make decisions
#   * Store and manage data with dictionaries
#   * Create interactive loops that respond to user input

# ==========================================
# Exercise 1: Simple if Statements
# ------------------------------------------
# Create a variable age = 18
# Write an if statement that prints "You are old enough to vote!"
# if age is greater than or equal to 18.
# Otherwise, print "You are not old enough to vote yet."

def checkAge():
    age = 18

    if age >= 18:
        print("You are old enough to vote!")
    else: 
        print("You are not old enough to vote yet.")


# ==========================================
# Exercise 2: if-elif-else Chains
# ------------------------------------------
# Create a variable temperature = 25
# Write an if-elif-else chain that:
#   * prints "It's cold!" if temperature < 10
#   * prints "It's mild." if temperature is between 10 and 25
#   * prints "It's hot!" if temperature > 25

def checkTemperature():
    temperature = 25

    if temperature < 10:
        print("It's cold!")
    elif 10 <= temperature <= 25:
        print("It's mild.")
    else:
        print("It's hot!")

# ==========================================
# Exercise 3: Boolean Expressions
# ------------------------------------------
# Create two variables: is_raining = True and have_umbrella = False
is_raining = True
have_umbrella = False
# Write an if-else statement:
#   * If it's raining and you have an umbrella, print "You're good to go!"
#   * If it's raining and you don't have one, print "You might get wet!"
#   * Otherwise, print "No rain today!"

def checkWeather():
    if is_raining and have_umbrella:
        print("You're good to go!")
    elif is_raining and not have_umbrella:
        print("You might get wet!")
    else:
        print("No rain today!")


# ==========================================
# Exercise 4: Using if with Lists
# ------------------------------------------
# Create a list of fruits = ['apple', 'banana', 'cherry']
fruits = ['apple', 'banana', 'cherry']
# Ask the user to input a fruit name.
# If the fruit is in the list, print "Yes, we have that!"
# Otherwise, print "Sorry, we don't have that."

def checkFruitAvailability():
    fruitInput = str(input("Enter a fruit name: ")).lower()
    if fruitInput in fruits:
        print("Yes, we have that!")
    else:
        print("Sorry, we don't have that.")

# ==========================================
# Exercise 5: Dictionaries - Basics
# ------------------------------------------
# Create a dictionary called person with keys: 'name', 'age', and 'city'.
# Print each key-value pair in a formatted sentence, e.g.:
#   "Name: Alice, Age: 25, City: London"

def printPersonInfo():
    person = {'name': 'Alice', 'age': 25, 'city': 'London'}
    print(f"Name: {person['name']}, Age: {person['age']}, City: {person['city']}")

# ==========================================
# Exercise 6: Adding and Modifying Dictionary Entries
# ------------------------------------------
# Add a new key 'occupation' with a value to your dictionary.
# Change the value of 'city' to something new.
# Print the updated dictionary.

def updatePersonInfo():
    person = {'name': 'Alice', 'age': 25, 'city': 'London'}
    person['occupation'] = 'Engineer'
    person['city'] = 'New York'
    print(person)

# ==========================================
# Exercise 7: Using get() Safely
# ------------------------------------------
# Try to access a key called 'country' using person.get('country', 'Not specified').
# Print the result.

def getCountryInfo():
    person = {'name': 'Alice', 'age': 25, 'city': 'London'}
    country = person.get('country', 'Not specified')
    print(f"Country: {country}")

# ==========================================
# Exercise 8: Looping Through a Dictionary
# ------------------------------------------
# Create a dictionary of favorite_languages:
#   favorite_languages = {'Alice': 'Python', 'Bob': 'C', 'Charlie': 'JavaScript'}
# Loop through the dictionary and print:
#   "Alice's favorite language is Python."

def printFavoriteLanguages():
    favorite_languages = {'Alice': 'Python', 'Bob': 'C', 'Charlie': 'JavaScript'}
    for name, language in favorite_languages.items():
        print(f"{name}'s favorite language is {language}.")

# ==========================================
# Exercise 9: Nesting - Dictionaries in Dictionaries
# ------------------------------------------
# Create a dictionary users = {
#     'alice': {'age': 25, 'city': 'London'},
#     'bob': {'age': 30, 'city': 'New York'}
# }
# Loop through the dictionary and print each user's name and details.

def printUserDetails():
    users = {
        'alice': {'age': 25, 'city': 'London'},
        'bob': {'age': 30, 'city': 'New York'}
    }
    for username, details in users.items():
        age = details['age']
        city = details['city']
        print(f"Username: {username}, Age: {age}, City: {city}")

# ==========================================
# Exercise 10: User Input
# ------------------------------------------
# Ask the user for their name using input().
# Greet them by name, e.g. "Hello, Sam!"

def greetUser():
    name = input("What is your name? ")
    print(f"Hello, {name}!")

# ==========================================
# Exercise 11: Using int() and Modulo Operator
# ------------------------------------------
# Ask the user for a number using input().
# Convert it to an integer.
# If the number is even, print "That’s an even number!"
# Otherwise, print "That’s an odd number!"

def checkEvenOdd():
    number = int(input("Enter a number: "))
    if number % 2 == 0:
        print("That’s an even number!")
    else:
        print("That’s an odd number!")

# ==========================================
# Exercise 12: while Loops
# ------------------------------------------
# Write a while loop that asks for input repeatedly until the user types 'quit'.
# Echo back each message they type (except 'quit').

def echoUntilQuit():
    while True:
        message = input("Type something (or 'quit' to stop): ")
        if message.lower() == 'quit':
            break
        print(f"You typed: {message}")

# ==========================================
# Exercise 13: Using Flags and break
# ------------------------------------------
# Modify the previous exercise using a flag (e.g., active = True).
# Inside the loop, if the user types 'quit', set active = False to stop the loop.

# ==========================================
# Exercise 14: while Loops with Lists
# ------------------------------------------
# Create a list of unconfirmed_users = ['alice', 'bob', 'charlie']
# and an empty list confirmed_users = []
# Use a while loop to move each user from unconfirmed_users to confirmed_users.
# Print messages confirming each user has been verified.

def confirmUsers():
    unconfirmed_users = ['alice', 'bob', 'charlie']
    confirmed_users = []

    while unconfirmed_users:
        current_user = unconfirmed_users.pop(0)
        print(f"Verifying user: {current_user}")
        confirmed_users.append(current_user)

    print("All users have been confirmed:")
    for user in confirmed_users:
        print(user)

# ==========================================
# Final Challenge: Interactive Program
# ------------------------------------------
# Create a small dictionary of menu items with prices, e.g.:
#   menu = {'coffee': 2.5, 'tea': 2.0, 'cake': 3.5}
# Write a program that:
#   * Repeatedly asks the user to enter an item or 'quit' to stop.
#   * If the item exists, print its price.
#   * If not, print "Sorry, we don't have that."
#   * When the user quits, thank them for visiting.

def cafeMenu():
    menu = {'coffee': 2.5, 'tea': 2.0, 'cake': 3.5}
    while True:
        item = input("Enter a menu item (or 'quit' to stop): ").lower()
        if item == 'quit':
            print("Thank you for visiting!")
            break
        elif item in menu:
            price = menu[item]
            print(f"The price of {item} is ${price:.2f}")
        else:
            print("Sorry, we don't have that.")

cafeMenu()
# ==========================================