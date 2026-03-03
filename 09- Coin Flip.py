import random

num = random.randint(0, 1)   # Roll a random number that's either 0 or 1

if num > 0.5:        # if statement is used to test a condition for truth
  print('Heads')     # If the conditional variable is TRUE code is executed, if is FALSE it is skipped
else:                # Could be added as an optional for if statement
  print('Tails')     # If the conditional variable is TRUE code is executed, if is FALSE the else part is executed
  