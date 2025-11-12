# Week 5: Functions
# Learning Objectives:
# - Define and use functions.
# - Pass arguments (positional, keyword, and with default values).
# - Return values from functions.
# - Work with lists inside functions.
# - Use *args and **kwargs.
# - Organize code into modules.

# =============================
# EXERCISE 1: Defining Functions
# =============================
# Task: Define a simple function called greet_user() that prints a greeting.
# Call it twice with different names.

def greet_user():
    print(f"Hello!")

greet_user()

# =============================
# EXERCISE 2: Passing Arguments
# =============================
# Task: Modify greet_user() so it accepts one parameter 'name' and prints a personalized greeting.
# Call it using both positional and keyword arguments.

def greet_user(name):
    print(f"Hello, {name}!")

greet_user("Alice") # positional argument
greet_user(name="Bob") # keyword argument

# =============================
# EXERCISE 3: Default Values
# =============================
# Task: Give your function a default value for 'name' (e.g., 'Guest').
# Test calling it with and without providing a name.

def greet_user(name="Guest"):
    print(f"Hello, {name}!")

greet_user()
greet_user("Charlie")


# =============================
# EXERCISE 4: Returning Values
# =============================
# Task: Define a function called make_full_name(first, last) that returns a formatted full name.
# Print the returned value.

def make_full_name(first, last):
    full_name = f"{first} {last}"
    return full_name.title()

print(make_full_name("ada", "lovelace"))

# =============================
# EXERCISE 5: Returning a Dictionary
# =============================
# Task: Modify make_full_name() to return a dictionary with keys 'first' and 'last'.
# Print the result.

def make_full_name_dict(first, last):
    person = {'first': first, 'last': last}
    return person

print(make_full_name_dict("Ada", "Lovelace"))


# =============================
# EXERCISE 6: Working with Lists
# =============================
# Task: Define a function called print_models(models_to_print) that loops through and prints each model name.
# Pass in a list of model names. Observe how lists behave when passed to functions.

def print_models(models_to_print):
    print("Printing models:")
    while models_to_print:
        current = models_to_print.pop()
        print(current)

print_models(['Model X', 'Model Y', 'Model Z'])

# =============================
# EXERCISE 7: Preventing Modification

# =============================
# Task: Modify print_models() to work on a *copy* of the list so the original is not changed.
# Hint: Pass models_to_print[:] to the function.

def print_models_safe(models_to_print):
    print("Printing models (safe copy):")
    for model in models_to_print:
        print(model)

print_models_safe(['Model A', 'Model B', 'Model C'])
# =============================
# EXERCISE 8: Arbitrary Arguments
# =============================
# Task: Define a function called make_pizza(*toppings) that prints all the toppings requested.
# Call it with different numbers of arguments.

def make_pizza(*toppings):
    print("Making a pizza with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")

make_pizza('pepperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')

# =============================
# EXERCISE 9: Arbitrary Keyword Arguments
# =============================
# Task: Define a function called build_profile(first, last, **info) that stores any number of keyword-value pairs.
# Test it with different pieces of user data.

def build_profile(first, last, **info):
    profile = {'first_name': first, 'last_name': last}
    profile.update(info)
    return profile

user_profile = build_profile('albert', 'einstein',
                             location='princeton',
                             field='physics')

print(user_profile)

# =============================
# EXERCISE 10: Modules
# =============================
# Task: Create a separate Python file called 'my_functions.py' with a simple function (e.g., greet_user()).
# Import that function in this script and call it.
# Try importing:
#   - the whole module
#   - a specific function
#   - a function using an alias



# =============================
# BONUS CHALLENGE
# =============================
# Task: Combine what you’ve learned.
# Write a program that:
#   - Defines a function to collect user info (name, age, city)
#   - Stores it in a dictionary using **kwargs
#   - Prints a greeting using a function from another module
