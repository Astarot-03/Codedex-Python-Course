"""

Control flow is the order in which the program's code executes.
- if: statement tests a condition for truth and executes the code if it's True.
- elif: clause can be added between if and else. Add more options
- else: executes the code if none of the above is True.
Relational operators are used to compare two values: 
    == Equal to.
    != No equal to.
    > Higher than.
    >= Higher than or equal to.
    < Less than.
    <= Less than or equal to.
Logical operators are used to combine two or more conditions: and, or, not.

"""
print('============')
print('Sorting Hat')
print('============')

print('🦁 Gryffindor')
print('🦅 Ravenclaw')
print('🦡 Hufflepuff')
print('🐍 Slytherin')

Gryffindor = 0
Ravenclaw = 0
Hufflepuff = 0
Slytherin = 0


print('Q1) Do you like Dawn or Dusk?')

print('  1) Dawn')
print('  2) Dusk')

Q1 = int(input('Enter your answer (1-2): '))

if Q1 == 1:
  Gryffindor = Gryffindor + 1  
  Ravenclaw = Ravenclaw + 1
elif Q1 == 2:
  Hufflepuff = Hufflepuff + 1
  Slytherin = Slytherin + 1
else:
  print("Wrong input.")

print('Q2) When I’m dead, I want people to remember me as?')

print('  1) The Good')
print('  2) The Great')
print('  3) The Wise')
print('  4) The Bold\n')

Q2 = int(input('Enter your answer (1-4): '))

if Q2 == 1:
  Hufflepuff = Hufflepuff + 2
elif Q2 == 2:
  Slytherin = Slytherin + 2
elif Q2 == 3:
  Ravenclaw = Ravenclaw + 2
elif Q2 == 4:
  Gryffindor = Gryffindor + 2
else:
  print("Wrong input.")
  
print('Q3) Which kind of instrument most pleases your ear?')

print('  1) The violin')
print('  2) The trumpet')
print('  3) The piano')
print('  4) The drum')


Q3 = int(input('Enter your answer (1-4): '))

if Q3 == 1:
  Slytherin = Slytherin + 4
elif Q3 == 2:
  Hufflepuff = Hufflepuff + 4
elif Q3 == 3:
  Ravenclaw = Ravenclaw + 4
elif Q3 == 4:
  Gryffindor = Gryffindor + 4
else:
  print("Wrong input.")


print("Gryffindor: ", Gryffindor)
print("Ravenclaw: ", Ravenclaw)
print("Hufflepuff: ", Hufflepuff)
print("Slytherin: ", Slytherin)


if Gryffindor >= Ravenclaw and Gryffindor >= Hufflepuff and Gryffindor >= Slytherin:
  print('====🦁 Gryffindor===')
elif Ravenclaw >= Hufflepuff and Ravenclaw >= Slytherin:
  print('===🦅 Ravenclaw===')
elif Hufflepuff >= Slytherin:
  print('===🦡 Hufflepuff===')
else:
  print('===🐍 Slytherin===')