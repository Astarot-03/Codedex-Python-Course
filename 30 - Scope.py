"""
Scope: dertermines when a variable is visible in a program and where it can be accessed. In Python, there are four types of variable scopes: local, enclosing, global, and built-in.


answer = 0 # global variable

def add(x, y):
  answer = x + y
  return answer # local variable

add(3, 4)

print(answer)

Output: 0

if two variables have the same name, the one in the local variable will be used inside the function.
The global variable with the same name will remain global and with the original value. 
"""


"""
In fintech, we often perform a time series analysis on stocks. This means that we need to analyze a stock, given its price over a certain time. 📈

In this exercise, we will perform a simplified version of a time series analysis. The stock that we will be analyzing is the $AMC stock in January 2023.

Here are the stock prices (in dollars) for each of these weekdays:

stock_prices = [34.68, 36.09, 34.94, 33.97, 34.68, 35.82, 43.41, 44.29, 44.65, 53.56, 49.85, 48.71, 48.71, 49.94, 48.53, 47.03, 46.59, 48.62, 44.21, 47.21]

Create a stock_analysis.py program that implements three functions:

price_at(x) that finds the price on a given day x.
max_price(a, b) that finds the maximum price from day a to day b.
min_price(a, b) that finds the minimum price from day a to day b.
The parameters of the days will be in the range of 1 to 20 (since that is the period for the stock we are analyzing).

Make sure to call each function to test if your functions work correctly!
"""

stock_prices = [34.68, 36.09, 34.94, 33.97, 34.68, 35.82, 43.41, 44.29, 44.65, 53.56, 49.85, 48.71, 48.71, 49.94, 48.53, 47.03, 46.59, 48.62, 44.21, 47.21]

def price_at(i):
  return stock_prices[i-1]

def max_price(a, b):
  mx = 0
  for i in range(a, b + 1):
    mx = max(mx, price_at(i))
  return mx

def min_price(a, b):
  mn = price_at(a)
  for i in range(a, b + 1):
    mn = min(mn, price_at(i))
  return mn

print(max_price(1, 5))
print(min_price(5, 10))
print(price_at(3))

# With built-in functions

stock_prices = [34.68, 36.09, 34.94, 33.97, 34.68, 35.82, 43.41, 44.29, 44.65, 53.56, 49.85, 48.71, 48.71, 49.94, 48.53, 47.03, 46.59, 48.62, 44.21, 47.21]

def price_at(i):
    return stock_prices[i-1]

def max_price(a, b):
    return max(stock_prices[a-1:b])

def min_price(a, b):
    return min(stock_prices[a-1:b])

# Test the functions
print(max_price(1, 5))   # Should print the max price from days 1 to 5
print(min_price(5, 10))  # Should print the min price from days 5 to 10
print(price_at(3))