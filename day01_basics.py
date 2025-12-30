# Day 01 — Python Refresh (Basics)

print("Day 01: Python refresh started ✅")

name = input("Enter your name: ").strip()
age_text = input("Enter your age: ").strip()

# Convert age safely
if age_text.isdigit():
    age = int(age_text)
    print(f"Hello {name}! Next year you will be {age + 1}.")
else:
    print(f"Hello {name}! Age must be a number.")

# Quick practice: simple calculator
num1 = input("Enter first number: ").strip()
num2 = input("Enter second number: ").strip()

if num1.replace(".", "", 1).isdigit() and num2.replace(".", "", 1).isdigit():
    a = float(num1)
    b = float(num2)
    print("Sum:", a + b)
    print("Difference:", a - b)
    print("Product:", a * b)
    print("Division:", a / b if b != 0 else "Cannot divide by zero")
else:
    print("Please enter valid numbers.")
