"""
Instructions
“Are we there yet?” is a phrase that has existed for as long as there are children, vehicles, and road trips.

First, ask the user “Are we there yet?” using the input() function and store it in an answer variable.

Then, create a while loop that asks the user “Are we there yet?” again. Keep asking them this over and over until they respond with “Yes”.

The output could look something like this:

Are we there yet? One more hour
Are we there yet? Almost there
Are we there yet? Don't make me pull over
Are we there yet? Yes

"""


answer = input('Are we there yet?')


while answer != 'Yes':
    if answer == 'No':
        print("One more hour.")
    elif answer == 'Nop':
        print("Almost There")
    elif answer == "Nel":
        print("Don't make me pull over")
    else:
        print("Hmm, I didn't understand that.")
    answer = input('Are we there yet? ')
if answer == 'Yes':
  print('Yes')