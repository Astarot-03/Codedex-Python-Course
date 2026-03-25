"""
Module is any file with a .py extension. It can contain functions, classes, and variables that can be imported and used in other Python files. Modules help to organize code and promote reusability.
python has over 200 modules in its standard library, and you can also create your own modules or install third-party modules using package managers like pip.

random module is a built-in module in Python that provides functions for generating random numbers and performing random operations. It includes functions for generating random integers, floating-point numbers, and selecting random items from a list.


import random

dice = [1, 2, 3, 4, 5, 6]

print(random.choices(dice))

#output: [2] or [5] or any other number from the dice list

import random

dice = [1, 2, 3, 4, 5, 6]

print(random.choices(dice, k=3))
#output: [2, 5, 1] or [3, 4, 6] or any other combination of three numbers from the dice list
k parameter specifies the number of random choices to make from the list. In this case, it will return a list of 3 random numbers from the dice list.

Multiple Module Imports
You can import multiple modules in top of the code

import random
import math # math module provides mathematical functions and constants

we can also import them in one line separated by commas

import random, math

Instructions
A gambling machine was invented in Brooklyn around 1891. Players would insert a nickel and pull a lever. If it's a good poker hand, you win a free beer. Soon, many bars in the city had it. This was a precursor to the modern slot machine.

Create a slot_machine.py program using random.

The items are symbols of common fruits and sevens (7️⃣). In each round, the slot machine displays three random items. If there are three sevens, you win!

Final Program Output

Create a symbols list and include the following items: '🍒',' 🍇', '🍉', '7️⃣'.

Next, create a results variable that uses the .choices() method from the random module and get three random symbols. Make sure to import the required module at the top of the file!

Then, print each value from results, separated by | pipe characters:

🍉 | 🍒 | 🍇

Lastly, use an if/else statement:

If all of the list items in results are equal to '7️⃣', print "Jackpot! 💰".
Else, print "Thanks for playing!".
Bonus:

Rewrite this program with a play() function.
Add a while loop for the player to keep playing, round after round.
Ask the player for a 'Y' or 'N' input to keep playing with input().
"""

import random

def play():
  symbols = ['🍒',' 🍇', '🍉', '7️⃣']
  results = (random.choices(symbols, k=3))
  print(f'{results[0]} | {results[1]} | {results[2]}')
  if results == ['7️⃣', '7️⃣', '7️⃣']:
    print("Jackpot! 💰")
  else:
    print("Thanks for playing!")

while True:
  play()
  keep_playing = input("Do you want to play again? (Y/N): ").upper()
  if keep_playing != "Y":
    break