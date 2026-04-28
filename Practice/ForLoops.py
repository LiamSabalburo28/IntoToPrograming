print("Countdown from 10 to 1:")
for i in range(10, 0, -1):
    print(i)

print("\n-------------------\n")

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
total = 0

for num in numbers:
    total += num

print("Sum of the list:", total)

print("\n-------------------\n")

nums = [1, 2, 3, 4, 5]
squares = []

for n in nums:
    squares.append(n ** 2)

print("Squares of numbers:", squares)

print("\n-------------------\n")

user_string = input("Enter a string: ")
vowels = "aeiouAEIOU"
vowel_count = 0

for char in user_string:
    if char in vowels:
        vowel_count += 1

print("Number of vowels:", vowel_count)

print("\n-------------------\n")

number = int(input("Enter a number for multiplication table: "))

print(f"Multiplication table for {number}:")
for i in range(1, 11):
    print(f"{number} x {i} = {number * i}")

print("\n-------------------\n")

names = ["Alice", "Bob", "Charlie"]

for name in names:
    print(f"Hello, {name}!")