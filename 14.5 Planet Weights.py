"""
Instructions
The year is 2199... Humanity is now an interplanetary species, freely traveling across the solar system! 🚀

Create a weight conversion program that:

Asks the user for their Earth weight (as a float).
Asks the user for a planet number (as an int).
Then, use an if/elif/else statement to calculate the user's weight on the destination planet.

To calculate the user's weight:

destination weight=Earth weight × relative gravity
Number	Planet	Relative Gravity
1	Mercury	0.38
2	Venus	0.91
3	Mars	0.38
4	Jupiter	2.53
5	Saturn	1.07
6	Uranus	0.89
7	Neptune	1.14
If the user enters a planet number outside of 1 - 7, print a message that says 'Invalid number'
"""

weight = float(input('What is your weight on Earth: '))

print('On which planet are you?')
print('1) Mercury')
print('2) Venus')
print('3) Mars')
print('4) Jupiter')
print('5) Saturn')
print('6) Uranus')
print('7) Neptuno')

planet = int(input('select your planet (1-7): '))

if planet == 1:
  planet = weight * 0.38
  print('Destination weight: Mercury ' + str(planet)+'Kg') 
elif planet == 2:
  planet = weight * 0.91 
  print('Destination weight: Venus ' + str(planet)+'Kg') 
elif planet == 3:
  planet = weight * 0.38
  print('Destination weight: Mars ' + str(planet)+'Kg') 
elif planet == 4:
  planet = weight * 2.53
  print('Destination weight: Jupiter ' + str(planet)+'Kg') 
elif planet == 5:
  planet = weight * 1.07
  print('Destination weight: Saturn ' + str(planet)+'Kg') 
elif planet == 6:
  planet = weight * 0.89
  print('Destination weight: Uranus ' + str(planet)+'Kg') 
elif planet == 7:
  planet = weight * 1.14
  print('Destination weight: Neptune ' + str(planet)+'Kg') 
else:
  print('invalid Number')