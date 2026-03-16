"""
Parameters and Arguments


The parameter is the variable listed inside the parenthesis in the function definition (when we define the function).
The argument is the value sent to the function (when we call the function).

def happy_birthday(name): # name is the parameter
  print('Happy birthday to you')
  print('Happy birthday to you')
  print('Happy birthday dear ' + name )
  print('Happy birthday to you')

happy_birthday('Lillian') # 'Lillian' is the argument


"""
# option 1

distance = float(input('Distance in Km: '))
def distance_to_miles(distance):
  print(f'{distance / 1.609} miles')

distance_to_miles(distance)

# option 2

def distance_to_miles(distance):
    miles = distance / 1.609
    print(miles)

distance_to_miles(10000)