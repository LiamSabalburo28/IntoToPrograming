print("1. Numbers from 1 to 20 (stop at 15):")
for i in range(1, 21):
    if i == 15:
        break
    print(i)

print("\n2. Odd numbers from 1 to 30:")
for i in range(1, 31):
    if i % 2 == 0:
        continue
    print(i)

print("\n3. Loop with pass (placeholder):")
for i in range(5):
    if i == 3:
        pass
    print(i)

print("\n4. Countdown from 10 to 1 (skip 5):")
for i in range(10, 0, -1):
    if i == 5:
        continue
    print(i)

print("\n5. Sum until a negative number is found:")
numbers = [4, 7, 2, 9, -3, 5, 6]
total = 0

for num in numbers:
    if num < 0:
        break
    total += num

print("Sum:", total)