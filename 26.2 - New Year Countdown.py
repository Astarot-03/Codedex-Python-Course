"""
Instructions
Ring in the New Year! A New Year's Eve party doesn't feel complete without a countdown from 10 to 1.

Use a for loop that counts down by using the "step" value in range().

Inside the loop, print the numbers from 10 to 1, each on its own line.

When the loop finishes the countdown, print this exact string Happy New Year! 🥳.

The output should look like this:

10
9
8
7
6
5
4
3
2
1
Happy New Year! 🥳

Counting down from 10 to 1 on each line and then a Happy New Year message at the end.

Range (start, stop, step) is a built-in function in Python that generates a sequence of numbers. The start parameter is the starting point of the sequence (inclusive), the stop parameter is the end point of the sequence (exclusive), and the step parameter is the increment or decrement between each number in the sequence. In this case, we want to count down from 10 to 1, so we can use a step of -1 to decrement the numbers.
"""

for i in range(10,0,-1):
  print(i)
  if i == 1:
    print('Happy New Year! 🥳')