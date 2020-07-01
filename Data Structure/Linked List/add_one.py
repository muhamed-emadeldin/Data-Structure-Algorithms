#!/usr/bin/env python
'''
Problem Statement
You are given a non-negative number in the form of list elements. For example, the number 123 would be provided as arr = [1, 2, 3]. Add one to the number and return the output in the form of a new list.
'''

# Change the arr in-place
def add_one(arr):
    """
    :param: arr - list of digits representing some number x
    return a list with digits represengint (x + 1)
    """
    str_digit = ""
    for dig in arr:
        str_digit += str(dig)
    
    int_digit = int(str_digit)
    add_one = int_digit + 1
    return [int(x) for x in str(add_one)]

print(add_one([1,2,1,3]))