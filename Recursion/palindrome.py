#!/usr/bin/env python

"""
A palindrome is a word that is the reverse of itself—that is, it is the same word when read forwards and backwards.

For example:

"madam" is a palindrome
"abba" is a palindrome
"cat" is not
"a" is a trivial case of a palindrome
"""

def is_palindrome(string):
  #basic condation
  if len(string) <= 1:
    return True
  
  else:
    first_char = string[0]
    last_char = string[-1]
    sup_string = string[1:-1]
    return (first_char == last_char) and is_palindrome(sup_string)

print ("Pass" if  (is_palindrome("")) else "Fail")
print ("Pass" if  (is_palindrome("a")) else "Fail")
print ("Pass" if  (is_palindrome("madam")) else "Fail")
print ("Pass" if  (is_palindrome("abba")) else "Fail")
print ("Pass" if not (is_palindrome("Udacity")) else "Fail")
