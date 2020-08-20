#!/usr/bin/env python

def binary_search(array, target):
    '''Write a function that implements the binary search algorithm using iteration
   
    args:
      array: a sorted array of items of the same type
      target: the element you're searching for
   
    returns:
      int: the index of the target, if found, in the source
      -1: if the target is not found
    '''
    #defense function
    if not isinstance(array, list):
      return None
    
    if target is None or target == "":
      return target

    #basic variables
    middle = len(array) // 2
    count = 0

    #check if len of array is even or odd
    if len(array) % 2 == 0:
      middle = middle - 1
    
    while middle <= len(array) or middle >= 0:
      #check if middle == target
      if array[middle] == target:
        return middle
      
      elif array[middle] < target:
        middle += 1
      
      else:
        middle -= 1
    
    return -1


def test_function(test_case):
    answer = binary_search(test_case[0], test_case[1])
    print(answer)
    if answer == test_case[2]:
        print("Pass!")
    else:
        print("Fail!")

array = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
target = 6
index = 6
test_case = [array, target, index]
test_function(test_case)