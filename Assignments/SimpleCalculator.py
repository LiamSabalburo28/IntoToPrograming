
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
   
    if y == 0:
        return "Error: Cannot divide by zero"
    return x / y



print("Simple Calculator")


x = float(input("Enter x: "))
y = float(input("Enter y: "))


print("\nResults:")
print("Add:", add(x, y))
print("Subtract:", subtract(x, y))
print("Multiply:", multiply(x, y))
print("Divide:", divide(x, y))