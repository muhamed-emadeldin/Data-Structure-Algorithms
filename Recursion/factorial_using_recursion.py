#!/usr/bin/env python

"""
The factorial function is a mathematical function that multiplies a given number,  𝑛 , and all of the whole numbers from  𝑛  down to 1.
"""

def factorial(n):
  #basic condation
  if n <= 1:
    return 1
  
  else:
    return n * factorial(n-1)

print ("Pass" if (1 == factorial(0)) else "Fail")
print ("Pass" if  (1 == factorial(1)) else "Fail")
print ("Pass" if  (24 == factorial(4)) else "Fail")