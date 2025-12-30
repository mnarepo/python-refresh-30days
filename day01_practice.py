# day01_practice.py
# Day 01 — Practice Tasks (Basics)

print("Day 01 Practice Started")

# -----------------------------------
# 1. Input 2 numbers → print larger one
# -----------------------------------
n1 = input("\nEnter first number: ").strip()
n2 = input("Enter second number: ").strip()

if n1.isdigit() and n2.isdigit():
    a = int(n1)
    b = int(n2)

    if a > b:
        print("Larger number:", a)
    else:
        print("Larger number:", b)
else:
    print("Invalid input. Numbers only.")


# -----------------------------------
# 2. Input a number → print even/odd
# -----------------------------------
num = input("\nEnter a number: ").strip()

if num.isdigit():
    num = int(num)
    if num % 2 == 0:
        print("Even number")
    else:
        print("Odd number")
else:
    print("Invalid input.")


# -----------------------------------
# 3. Input a year → leap year or not
# -----------------------------------
year = input("\nEnter a year: ").strip()

if year.isdigit():
    year = int(year)
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        print("Leap Year")
    else:
        print("Not a Leap Year")
else:
    print("Invalid year input.")


# -----------------------------------
# 4. Input a string → length + first/last
# -----------------------------------
text = input("\nEnter a string: ").strip()

if text:
    print("Length:", len(text))
    print("First character:", text[0])
    print("Last character:", text[-1])
else:
    print("Empty string entered.")


# -----------------------------------
# 5. Input 3 numbers → print max
# -----------------------------------
x = input("\nEnter first number: ").strip()
y = input("Enter second number: ").strip()
z = input("Enter third number: ").strip()

if x.isdigit() and y.isdigit() and z.isdigit():
    x = int(x)
    y = int(y)
    z = int(z)

    max_num = x
    if y > max_num:
        max_num = y
    if z > max_num:
        max_num = z

    print("Maximum number:", max_num)
else:
    print("Invalid input.")


# -----------------------------------
# 6. Convert Celsius to Fahrenheit
# -----------------------------------
celsius = input("\nEnter temperature in Celsius: ").strip()

if celsius.replace(".", "", 1).isdigit():
    celsius = float(celsius)
    fahrenheit = (celsius * 9 / 5) + 32
    print("Temperature in Fahrenheit:", fahrenheit)
else:
    print("Invalid temperature input.")


# -----------------------------------
# 7. Reverse a string
# -----------------------------------
word = input("\nEnter a string to reverse: ").strip()
print("Reversed string:", word[::-1])


# -----------------------------------
# 8. Count vowels in a string
# -----------------------------------
sentence = input("\nEnter a string: ").strip()
vowels = "aeiouAEIOU"
count = 0

for ch in sentence:
    if ch in vowels:
        count += 1

print("Number of vowels:", count)
