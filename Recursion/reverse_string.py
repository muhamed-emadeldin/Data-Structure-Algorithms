#!/usr/bin/env python

"""
The goal in this notebook will be to get practice with a problem that is frequently solved by recursion: Reversing a string.

Note that Python has a built-in function that you could use for this, but the goal here is to avoid that and understand how it can be done using recursion instead.
"""

def reverse_string(string):
  #basic condation
  if len(string) == 0:
    return ""
  
  else:
    #basic variables
    fisrt_char = string[0]
    slice_char = slice(1, None)
    sub_string = string[slice_char]
    return reverse_string(sub_string) + fisrt_char

# print ("Pass" if  ("" == reverse_string("")) else "Fail")
# print ("Pass" if  ("cba" == reverse_string("abc")) else "Fail")
print ("Pass" if  ("sana" == reverse_string("anas")) else "Fail")


  