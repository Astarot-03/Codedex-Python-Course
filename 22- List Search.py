"""
Index: List items are changeable, meaning we can update individual items within a list.
An index is an item's position in a list.

Python is 0-indexed, meaning that the indices starts at 0:

vowels = ['a', 'e', 'i', 'o', 'u']
# Index:   0    1    2    3    4

Index can be negative starting in -1 with the last item in the list:

vowels = ['a', 'e', 'i', 'o', 'u']
# Index:   0    1    2    3    4
# Index:  -5   -4   -3   -2   -1

Slicing: is use to get more than one item on a list, we can get access to acertain part of the list
instead of using a singular index variable we can use a slice name[start : end].

vowels = ['a', 'e', 'i', 'o', 'u']

print(vowels[0 : 3]) it will not take the last index, it will take the index before the last one, in this case it will take the index 0, 1 and 2 but not 3.

print(vowels[1 : 3])

# Output:
# ['a', 'e', 'i']
# ['e', 'i']
"""

todo = ['🏦 Get quarters.',
       '🧺 Do laundry.',
       '🌳 Take a walk.',
       '💈 Get a haircut.',
       '🍵 Make some tea.',
       '💻 Complete Lists chapter.',
       '💖 Call mom.',
       '📺 Watch My Hero Academia.',]

print(todo[0]) # index
print(todo[1]) # index
print(todo[2 : 5]) # Slicing