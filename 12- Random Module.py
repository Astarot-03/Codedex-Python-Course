
# Random module
# Python has more than 200 modules, one of them call random
# First we need to import the module (import) (module) 'import random'
# Randint function generate a random number from a range '.randint(range separate by comma)


import random

Question = input('Question: ')

num = random.randint(1, 9)


if num == 1:
  answer = 'Yes - definitely.'
elif num == 2:
  answer = 'It is decidedly so.'
elif num == 3:
  answer = 'Without a doubt.'
elif num == 4:
  answer = 'Reply hazy, try again.'
elif num == 5:
  answer = 'ask again later.'
elif num == 6:
  answer = 'Better not tell you now.'
elif num == 7:
  answer = 'My sources say no.'
elif num == 8:
  answer = 'Outlook not so good.'
else:
  answer = 'Very doubtful.'


print('Magic 8 ball: ' + answer)