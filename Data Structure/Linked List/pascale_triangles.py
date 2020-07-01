#!/usr/bin/env python

"""
Problem Statement
Find and return the nth row of Pascal's triangle in the form a list. n is 0-based.
For exmaple, if n = 4, then output = [1, 4, 6, 4, 1].
To know more about Pascal's triangle: https://www.mathsisfun.com/pascals-triangle.html
"""

def nth_row_pascal(n):
  #basic variables
  list_append= []
  #basic of pascale triangle
  list_pascale = [0] + [1] + [0]

  #defense condation
  if n is None:
    return None

  #basic case
  if n == 0:
    return list_pascale[1:-1]

  else:
    for i in range(n):
      for row in range(1, len(list_pascale)):
        list_append += [list_pascale[row-1] + list_pascale[row]]
      
      list_pascale = [0] + list_append + [0]
      list_append =[]

  return list_pascale[1:-1]

print(nth_row_pascal(2))

