# =========================================
# Week 7 — Introduction to Object-Oriented Programming (OOP)
# Save as exercises7.py
#
# Topics:
#   - Classes and Objects
#   - The __init__() method
#   - Working with attributes and methods
#   - Setting and modifying attribute values
# =========================================

# -------------------------------------------------
# Task A: Creating a Simple Class (25 mins)
# -------------------------------------------------
# 1. Define a class called 'Car'.
# 2. Add an __init__() method with three attributes:
#       - make
#       - model
#       - year
# 3. Create two car objects (instances) and print their attributes.
# 4. Add a __str__() method to display car details neatly when printed.

# Example:
#   car1 = Car("Toyota", "Corolla", 2020)
#   print(car1)
# Expected output: "2020 Toyota Corolla"
'''
class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def __str__(self):
        return f"{self.year} {self.make} {self.model}"

car1 = Car("Toyota", "Corolla", 2020)
car2 = Car("Honda", "Civic", 2019)

print(car1)
print(car2)
'''
# -------------------------------------------------
# Task B: Adding Methods and Default Attributes (30 mins)
# -------------------------------------------------
# 1. Extend the Car class with:
#       - a default attribute: odometer_reading = 0
#       - a method 'read_odometer()' that prints the current mileage
#       - a method 'update_odometer(mileage)' that sets a new mileage
#         (prevent reducing the odometer!)
#       - a method 'increment_odometer(miles)' that adds to mileage
# 2. Demonstrate these methods by creating a car, updating mileage,
#    and printing results.

'''
class Car:
    def __init__ (self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def __str__(self):
        return f"{self.year} {self.make} {self.model}"
    
    def read_odometer(self):
        print(f"This car has {self.odometer_reading} miles")
    
    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't reduce the odometer reading")
    
    def increment_odometer(self, miles):
        self.odometer_reading += miles

car1 = Car("Toyota", "Corolla", 2020)
car1.update_odometer(20000)
car1.read_odometer()
car1.increment_odometer(100)
car1.read_odometer()
car1.update_odometer(15000)  # WARNING MESSAGE
'''
# -------------------------------------------------
# Task C: Mini Project – Student Record System (35 mins)
# -------------------------------------------------
# 1. Create a class called 'Student' with attributes:
#       - first_name
#       - last_name
#       - student_id
#       - grades (a list, default empty)
# 2. Add methods:
#       - add_grade(grade)
#       - average_grade() — returns the mean of all grades
#       - __str__() — prints student details and average
# 3. Create several Student objects and add grades for each.
# 4. Store all students in a list and print a report showing their details.
#
# Extension:
#   - Create a method 'is_passing()' that returns True if average >= 50.
#   - Print only passing students.

class Student:
    def __init__ (self, first_name, last_name, student_id):
        self.first_name = first_name
        self.last_name = last_name
        self.student_id = student_id
        self.grades = []
    
    def add_grade(self, grade):
        self.grades.append(grade)
    
    def average_grade(self):
        if self.grades:
            return sum(self.grades) / len(self.grades)
    
    def __str__ (self):
        avg = self.average_grade()
        avg_str = f"{avg:.2f}" if avg is not None else "N/A"
        return f"Student ID: {self.student_id}, Name: {self.first_name} {self.last_name}, Average Grade: {avg_str}"
    
    def is_passing(self):
        avg = self.average_grade()
        return avg is not None and avg >= 50
    
# Creating student objects
student1 = Student("Alice", "Smith", "S001")
student1.add_grade(85)
student1.add_grade(90)
student1.add_grade(78)
student2 = Student("Bob", "Johnson", "S002")
student2.add_grade(45)
student2.add_grade(55)
student2.add_grade(60)
student3 = Student("Charlie", "Brown", "S003")
student3.add_grade(30)
student3.add_grade(40)
student3.add_grade(50)

# Storing students in a list
students = [student1, student2, student3]

print("All Students:")
for student in students:
    print(student)
print("\nPassing Students:")
for student in students:
    if student.is_passing():
        print(student)
