"""
Nested List: A list can contain other lists as its elements. This is called a nested list.

list = ['a', 'b', 'c', [1, 2, 3]]

To access elements in a nested list, we use extra square brackets. The first set of square brackets is used to access the inner list, and the second set is used to access the element within that inner list.

list = ['a', 'b', 'c', [1, 2, 3]]

print(list[3][1])

output: 2

Matrix: If we create a list and every item in the list is also a list, we can call it a matrix. A matrix is a 2D array that can be used to represent data in rows and columns.
matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
or 
matrix = [[1, 2, 3, 4],
            [5, 6, 7, 8],
            [9, 10, 11, 12]]
or even 
matrix = [
  [1, 2, 3, 4],
  [5, 6, 7, 8],
  [9, 10, 11, 12]
]
example of a tic-tac-toe board:

board = [
  ['x', ' ', ' '],
  [' ', 'x', ' '],
  ['o', 'x', 'o']
]
board[0][0] board[0][1] board[0][2]
board[1][0] board[1][1] board[1][2]
board[2][0] board[2][1] board[2][2]

"""

board = [
  ['x', ' ', ' '],
  [' ', 'x', ' '],
  ['o', 'x', 'o']
]


row = 2
column = 2

print(board[row][column])
# Output: x