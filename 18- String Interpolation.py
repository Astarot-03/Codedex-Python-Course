"""
String concatenation

for i in range(5):
  print('The square of ' + str(i) + ' is ' + str(i*i))

String Interpolation

for i in range(5):
  print(f'The square of {i} is {i*i}')

To simplify the concatenation we use interpolation, in this example instead of using str() and + sign
we can make it easy to read with f' that will simplify the code

To make range goes decending we add the higher value then the lower number and then the amount of steps we are doing
range(99,0,-1)

"""


for i in range(99,0,-1):
  print(f'{i} bottles of beer on the wall')

  print(f'{i} bottles of beer')

  print('take one down, pass it around')
  
  print(f'{i-1} bottles of beer on the wall')