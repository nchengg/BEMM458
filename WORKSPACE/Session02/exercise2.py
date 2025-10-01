# ======================================
# Python Exercises: Lists, Loops & Tuples
# ======================================
# Save this file as exercises2.py
# Topics covered:
# - Lists and Tuples
# - Organizing and modifying lists
# - Looping through data
# - Using range() and comprehensions
# - Basic statistics
# - Slicing
# - Code styling (PEP 8)
# Learning Objectives:
#   * Store and manipulate collections of data.
#   * Automate repetitive tasks with loops.
#   * Follow basic Python style guidelines.

# ======================================
# 1. Defining and Accessing Lists
# --------------------------------------
# Create a list called fruits with at least three fruit names.
# Print the list.
# Print the first and last items using their index.

import random


fruits = ["apple", "banana", "cherry"]
print(fruits)
print(fruits[0])
print(fruits[-1])

# ======================================
# 2. Modifying Lists
# --------------------------------------
# Change the value of the first fruit in your list.
# Add a new fruit to the end of the list using append().
# Insert a fruit at the beginning using insert().
# Remove one fruit using del, one using pop(), and one using remove().
# Print the updated list.

fruits[0] = "orange"
fruits.append("mango")
fruits.insert(0, "kiwi")
del fruits[1]
fruits.pop()
fruits.remove("cherry")
print(fruits)

# ======================================
# 3. Organizing Lists
# --------------------------------------
# Create a list of three or more country names.
# Print the list in alphabetical order using sorted().
# Print the original list to show it is unchanged.
# Sort the list permanently using sort() and print it again.
# Print the list in reverse order using reverse().
# Print the number of countries in the list using len().

countries = ["Canada", "Brazil", "Australia", "Denmark"]
print(sorted(countries))
print(countries)
countries.sort()
print(countries)
countries.reverse()
print(countries, len(countries))

# ======================================
# 4. Avoiding Index Errors
# --------------------------------------
# Try to print an element at an index that doesn’t exist.
# Wrap your code in a try/except block to handle the error gracefully.

try:
    print(countries[10])
except IndexError:
    print("Index out of range")

# ======================================
# 5. Looping with for
# --------------------------------------
# Create a list of animals and use a for loop to print each animal’s name.
# Add a message after the loop to thank the user.

animals = ["dog", "cat", "rabbit"]
for animal in animals:
    print(animal)
print("Thank you for visiting!")

# ======================================
# 6. Numerical Lists
# --------------------------------------
# Use range() to generate a list of numbers from 1 to 10.
# Print each number using a for loop.
# Create a list of even numbers between 2 and 20 using range().
# Use min(), max(), and sum() to print statistics about your list.

numbers = list(range(1, 11))
for number in numbers:
    print(number)

evenList = []
for even in numbers:
    if even % 2 == 0:
        evenList.append(even)

print(evenList)

# ======================================
# 7. List Comprehensions
# --------------------------------------
# Use a list comprehension to create a list of squares (1 to 10).
# Print the list.

squares = [x**2 for x in range(1, 11)]
print(squares)

# ======================================
# 8. Slicing Lists
# --------------------------------------
# Create a list of your favourite foods.
# Print the first three items, middle three items, and last three items using slices.
# Loop through a slice of the list (e.g., first three items) and print each item.
# Make a copy of the list using slicing and modify one of them.

foods = ["pizza", "sushi", "burger", "pasta", "salad", "taco", "steak"]
print(foods[:3])
print(foods[2:5])
print(foods[-3:])

for food in foods[:3]:
    print(food)

foods.append("salad")

# ======================================
# 9. Tuples
# --------------------------------------
# Create a tuple called dimensions with two values (width, height).
# Print each value using a loop.
# Try changing one of the values (should cause an error) and note what happens.
# Reassign the tuple to a new pair of values and print it again.

dimensions = (1920, 1080)
for i in dimensions:
    print(i)

# ======================================
# 10. Code Styling (PEP 8)
# --------------------------------------
# Review your code and ensure:
# - Indentation is 4 spaces
# - Lines are under 79 characters
# - Use blank lines to separate logical sections
# This exercise is for self-review.

# ======================================
# Final Challenge
# --------------------------------------
# Create a program that:
#   1. Creates a list of favourite movies.
#   2. Prints them sorted alphabetically.
#   3. Loops through and prints each movie with a custom message.
#   4. Creates a tuple of movie ratings (1–5) and prints the average rating.
#   5. Ensures your program follows PEP 8 guidelines.

movies = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]

movies.sort()
print(movies)

for movie in movies:
    print("Movie: ", movie , ", is recommended")

ratings = (random.randint(1, 5) for _ in range(len(movies)))

for movie in movies:
    print("Movie: ", movie , ", rating: ", next(ratings))