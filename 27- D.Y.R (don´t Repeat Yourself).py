"""
Create a dry.py program and check out the complete list of built-in functions:

Find 4 built-in functions that we have used previously in the course.
Pick 1 built-in function that we have not seen before.
Use each of these once in the program.

For the new function, try to read the documentation (😵‍💫) or Google it (👍)!

Add a comment for each built-in function to explain how they work.

print('Hello, world!') # Print: function to print a string to the console
name = input('What´s your name?') # Input: function to get user input from the console
level = int(input('what´s your level? ')) # Int: function to convert a string to an integer
for i in range(5):  # Range: function to generate a sequence of numbers, starting from 0 by default, and increments by 1 (by default), and ends at a specified number
  print(i)
  
print(bin(10)) # Bin: function to convert an integer to a binary string

Define a Function: we create or define funtions for the code to do an specific task, we can reuse the code as many times as we want, and it makes our code more organized and easier to read.
To define a function, we need a function definition. A function definition begins with the def keyword, followed by the function name, a set of parentheses, and a colon, in that order.

def say_hello():
  print('Hello') # the code inside the function is indented, and it will be executed when the function is called
  print('How are you')

to call a function, we simply write the function name followed by parentheses. We can call the same function as many times as we want, and it will execute the code inside the function each time it is called.

def say_hello():
  print('Hello') # the code inside the function is indented, and it will be executed when the function is called
  print('How are you')

say_hello()
say_hello()
say_hello() 


Fortune Cookie is a small cookie wafer with a piece of paper inside, called a “fortune”, which is usually a Chinese phrase with translation and a list of lucky numbers. They are served in restaurants in the U.S. and Canada. 🥠

Create a fortune_cookie.py program that gives the user random fortunes.

Define a function named fortune(). Inside the function, print out a random fortune from the list of options below:

Don't pursue happiness – create it.
All things are difficult before they are easy.
The early bird gets the worm, but the second mouse gets the cheese.
Someone in your life needs a letter from you.
Don't just think. Act!
Your heart will skip a beat.
The fortune you search for is in another cookie.
Help! I'm being held prisoner in a Chinese bakery!
Make sure to use the random module's random.randint() and an if/elif/else.

Then, call the fortune() function three times and see what you get!

Bonus: If you're daring, rewrite the function without an if/elif/else.
"""
# Option 1: Using if/elif/else
import random

def fortune():
  num = random.randint(1, 8)
  if num == 1:
    print("Don't pursue happiness – create it.")
  elif num == 2:
    print("All things are difficult before they are easy.")
  elif num == 3:
    print("The early bird gets the worm, but the second mouse gets the cheese.")
  elif num == 4:
    print( "Someone in your life needs a letter from you.")
  elif num == 5:
    print("Don't just think. Act!")
  elif num == 6:
    print("Your heart will skip a beat.")
  elif num == 7:
    print("The fortune you search for is in another cookie.")
  else:  
    print("Help! I'm being held prisoner in a Chinese bakery!")

fortune()

# Option 2: Without using if/elif/else
import random

def fortune():
  fortunes = ["Don't pursue happiness – create it.",
             "All things are difficult before they are easy.",
             "The early bird gets the worm, but the second mouse gets the cheese.",
             "Someone in your life needs a letter from you.",
             "Don't just think. Act!",
             "Your heart will skip a beat.",
             "The fortune you search for is in another cookie.",
             "Help! I'm being held prisoner in a Chinese bakery!"]

  num = random.randint(0, 7)
  print(fortunes[num])

import random

def fortune():
  fortunes = ["Don't pursue happiness – create it.",
             "All things are difficult before they are easy.",
             "The early bird gets the worm, but the second mouse gets the cheese.",
             "Someone in your life needs a letter from you.",
             "Don't just think. Act!",
             "Your heart will skip a beat.",
             "The fortune you search for is in another cookie.",
             "Help! I'm being held prisoner in a Chinese bakery!"]

  num = random.randint(0, 7)
  print(fortunes[num])

fortune()
fortune()
fortune()

# Option 3: Other if/elif/else way, with the options list defined outside the function, and using the random.randint() function to select a random fortune from the list.
import random

options = [
  "Don't pursue happiness - create it.",
  "All things are difficult before they are easy.",
  "The early bird gets the worm, but the second mouse gets the cheese.",
  "If you eat something and nobody sees you eat it, it has no calories.",
  "Someone in your life needs a letter from you.",
  "Don't just think. Act!",
  "Your heart will skip a beat.",
  "The fortune you search for is in another cookie.",
  "Help! I'm being held prisoner in a Chinese bakery!"
]

def fortune():
  random_fortune = random.randint(0, len(options) - 1)

  if random_fortune == 0:
    option = options[0]
  elif random_fortune == 1:
    option = options[1]
  elif random_fortune == 2:
    option = options[2]
  elif random_fortune == 3:
    option = options[3]
  elif random_fortune == 4:
    option = options[4]
  elif random_fortune == 5:
    option = options[5]
  elif random_fortune == 6:
    option = options[6]
  elif random_fortune == 7:
    option = options[7]
  elif random_fortune == 8:
    option = options[8]
  else:
    option = 'Error'

  print(option)

fortune()
fortune()
fortune()

# Option 4: defing the list of fortunes outside the function, and using the random.choice() function to select a random fortune from the list.
import random

options = [
  "Don't pursue happiness - create it.",
  "All things are difficult before they are easy.",
  "The early bird gets the worm, but the second mouse gets the cheese.",
  "If you eat something and nobody sees you eat it, it has no calories.",
  "Someone in your life needs a letter from you.",
  "Don't just think. Act!",
  "Your heart will skip a beat.",
  "The fortune you search for is in another cookie.",
  "Help! I'm being held prisoner in a Chinese bakery!"
]

def fortune():
  random_fortune = random.randint(0, len(options) - 1)
  print(options[random_fortune])

fortune()
fortune()
fortune()