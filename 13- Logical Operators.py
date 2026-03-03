
# Logical Operators
# Known as a Boolean operators, combine and evaluate two conditions
# - and: Return True if both conditions are True, return False otherwise
# - or: Return True if at least one of the conditions is true, and false otherwise
# - not: Return True if the condition is False, and vice versa
# A 	|   B	  |  A and B |	A or B
# False |	False |	 False	 | False
# False	|   True  |	 False	 | True
# True	|   False |	 False	 | True
# True	|   True  |	 True	 | True


height = int(input('What is your height?: '))
credits = int(input('how many credits do you have?: '))

if height >= 137 and credits >= 10:
  print('Enjoy thee ride!')
elif height < 137 and credits >= 10:
  print('You are not tall enough to ride.')
elif height >= 137 and credits < 10:
  print("you don't have enough credits.")
else:
  print("You don't meet the criteria to ride.")