"""
Loops: are used to repeat a code until a specific condition is complete or satisfied
while: is a a loop that while repete the code until the criteria is meet

A while loop looks very similar to an if statement. Just like an if statement, it executes the code if the condition is True.
However, the difference is that the while loop will continue to execute the code inside of it, over and over again, as long as the condition is True.

! is use as negation, while not guess = 6 is equal to while guess !=6

"""


print('BANK OF CODÉDEX')

pin = int(input('Enter your PIN: '))

while pin != 1234:
  pin = int(input('Incorrect PIN. Enter your PIN again: '))

if pin == 1234:
  print('PIN accepted!')