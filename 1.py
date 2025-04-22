import math
import time

# Task 1: Hello message with name
name = input("Enter your name: ")
print(f"Hello, {name}!")

# Task 2: Arithmetic operations
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
print(f"Sum: {num1 + num2}")
print(f"Difference: {num1 - num2}")
print(f"Product: {num1 * num2}")
try:
    print(f"Division: {num1 / num2}")
except ZeroDivisionError:
    print("Division: Error - Division by zero!")

# Task 3: Word and character count
text = input("Enter a string: ")
words = len(text.split())
chars = len(text)
print(f"Word count: {words}")
print(f"Character count: {chars}")

# Task 4: Area of shapes
shape = input("Enter shape (rectangle/triangle/circle): ").lower()
if shape == "rectangle":
    length = float(input("Enter length: "))
    width = float(input("Enter width: "))
    print(f"Area: {length * width}")
elif shape == "triangle":
    base = float(input("Enter base: "))
    height = float(input("Enter height: "))
    print(f"Area: {0.5 * base * height}")
elif shape == "circle":
    radius = float(input("Enter radius: "))
    print(f"Area: {math.pi * radius ** 2}")
else:
    print("Invalid shape!")

# Task 5: Print name n times
name = input("Enter name to print: ")
n = int(input("Enter number of times: "))
print("Using for loop:")
for _ in range(n):
    print(name)
print("Using while loop:")
count = 0
while count < n:
    print(name)
    count += 1

# Task 6: Print current time 10 times
for _ in range(10):
    print(time.ctime())
    time.sleep(10)

# Task 7: Read file and print word count per line
file_name = input("Enter file name: ")
try:
    with open(file_name, 'r') as file:
        for line in file:
            words = len(line.split())
            print(f"Line: {line.strip()} | Word count: {words}")
except FileNotFoundError:
    print("File not found!")
