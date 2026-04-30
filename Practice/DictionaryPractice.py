students = {"Alice": "A", "Bob": "B", "Charlie": "C", "David": "A", "Eve": "B"}
for name, grade in students.items():
    print(f"{name}: {grade}")

student = {"name": "Alice", "age": 16, "grade": "A"}
print(student["name"], student["age"])

student["grade"] = "A+"
print(student)

movies = {"Inception": 2010, "Titanic": 1997, "Avatar": 2009}
new_movie = input()
year = int(input())
movies[new_movie] = year
print(movies)

fruits = {"apple": 1.2, "banana": 0.5, "orange": 0.8, "grape": 2.0, "mango": 1.5}
remove_fruit = input()
if remove_fruit in fruits:
    del fruits[remove_fruit]
print(fruits)

inventory = {"apples": 10, "bananas": 5, "oranges": 8}
for fruit, qty in inventory.items():
    print(f"{fruit}: {qty}")

words = input().split()
counts = {}
for word in words:
    counts[word] = counts.get(word, 0) + 1
print(counts)

books = {
    "book1": {"title": "1984", "author": "George Orwell", "year": 1949},
    "book2": {"title": "To Kill a Mockingbird", "author": "Harper Lee", "year": 1960},
    "book3": {"title": "The Great Gatsby", "author": "F. Scott Fitzgerald", "year": 1925}
}
for book in books.values():
    print(book["title"], book["author"], book["year"])

squares = {i: i * i for i in range(1, 11)}
print(squares)

employees = {"Alice": 50000, "Bob": 60000, "Charlie": 55000}
max_employee = max(employees, key=employees.get)
print(max_employee, employees[max_employee])