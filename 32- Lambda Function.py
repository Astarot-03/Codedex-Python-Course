"""
lambda function is an anonymous function in Python that can take any number of arguments but can only have one expression. It is defined using the lambda keyword. The syntax for a lambda function is as follows:
lambda arguments: expression 

Lambda funtions are often used for short, simple functions that are not reused elsewhere in the code. They can be used in places where a function is required, such as in the map(), filter(), and reduce() functions, or as an argument to higher-order functions.

"""

def double(x):
  return x * 2

print(double(5))  # Output: 10

# Using a lambda function to achieve the same result

double_lambda = lambda x: x * 2 # we reduce the function to a single line using lambda

print(double_lambda(5))  # Output: 10