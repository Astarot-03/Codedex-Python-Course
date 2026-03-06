"""
The outer while loop runs as long as the not_found boolean variable is True.

For the inner for loop, we're iterating from 1 to 9. We stop early when the i variable is equal to the lucky_number.

To break out of the for loop, we use the break keyword. To break out of the outer while loop, we reassign False to the notFound variable.
"""

import random

# Generate a random lucky number between 1 and 9
lucky_number = random.randint(1,9)
# Flag to indicate if the lucky number has been found
not_found = True

# Outer while loop: continues until the lucky number is found
while not_found:
  # Inner for loop: iterate through numbers 1 to 9
  for i in range(1, 10):
    if i == lucky_number:
      # Lucky number found, set flag to False to exit loops
      not_found = False
      break
    else:
      # Print the current number if it's not the lucky number
      print(i)

# Print success message with the lucky number
print(f"Yay I got my lucky number {lucky_number}! 🍀")