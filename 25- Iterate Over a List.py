"""
Iterate over a list using a for-in loop and range() and len() functions.
For-in: use to loop through the items of a list directly.



snowfall = [0.3, 0.0, 0.0, 1.2, 3.9, 2.2, 0.8]

for i in snowfall:
  print(i)

output:
0.3
0.0
0.0
1.2
3.9
2.2
0.8

range() and len(): use to loop through the indices of a list.  
range() function returns a sequence of numbers, from 0 to a number.
len() function returns the length of the list.
  
for i in range(len(snowfall)):
  print(snowfall[i])

Output:
0.3
0.0
0.0
1.2
3.9
2.2
0.8


  """

playlist = [
  'The Beatles - Hey Jude!',
  'Metallica - Master Of Puppets',
  'Led Zeppelin - Stairway to Heave',
  'Deep Purple - Smoke on the Water',
  'Queen - Bohemian Rhapsody',
  'Heart - Alone'
]

for song in playlist:
  print(song)