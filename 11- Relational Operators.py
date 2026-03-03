
# Relational Operators
# == Equal to
# != Not equal to
# > Greater than
# < Less than
# >= Greater than or equal to
# <= Less than or equal to


grade = 90

if grade > 90:
  print('A')
elif grade > 80:
  print('B')
elif grade > 70:
  print('C')
elif grade > 60:
  print('D')
else:
  print('F')


# Elif short for (else if) optionally added between if and else to provide addtional condtion(s) to check

pH = int(input('Enter a pH value (0-14): '))

if pH > 7:
  print('Basic')
elif pH == 7:
  print('Neutro')
else:
  print('Acid')