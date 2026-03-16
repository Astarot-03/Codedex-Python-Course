"""
Return value is the value that a function call evaluates to. It is the output of the function. In Python, you can use the `return` statement to specify the value that a function should return. If a function does not have a `return` statement, it will return `None` by default. 
Here is an example of a function that returns a value:
def add(a, b):
  return a + b
In this example, the `add` function takes two parameters `a` and `b`, and returns their sum. When you call `add(3, 5)`, it will return `8`. You can also store the return value in a variable:
result = add(3, 5)
print(result)

8

return is used to send values from one point in a program to another. 
print is used to display values to the user.

"""

def add(a, b):
  return a + b

def subtract(a, b):
  return a - b

def multiply(a, b):
  return a * b

def divide(a, b):
  return a / b

def exp(a, b):
  return a ** b

print(add(3, 5))
print(subtract(7, 2))
print(multiply(4, 8))
print(divide(9, 3))
print(exp(2, 3))