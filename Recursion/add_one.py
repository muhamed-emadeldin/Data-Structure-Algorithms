#!/usr/bin/env python

"""
Problem Statement
You are given a non-negative number in the form of list elements. For example, the number 123 would be provided as arr = [1, 2, 3]. Add one to the number and return the output in the form of a new list.
"""

def add_one(arr):
  if arr == [9]:
    print("yes")
    return [1,0]
  
  if arr[-1] < 9:
    arr[-1] += 1
  
  else:
    print(add_one(arr[:-1]))
    return add_one(arr[:-1]) + [0]
  
  return arr

# A helper function for Test Cases
def test_function(test_case):
    arr = test_case[0]
    solution = test_case[1]
    
    output = add_one(arr)
    for index, element in enumerate(output):
        if element != solution[index]:
            print("Fail")
            return
    print("Pass")  

# Test Case 3
arr = [9, 9, 9]
solution = [1, 0, 0, 0]
test_case = [arr, solution]
test_function(test_case)