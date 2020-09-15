#!/usr/bin/env python

def rearrange_digits(input_list):
  #-->defense function
  assert(isinstance(input_list, list)), "AssertionError"

  for i in input_list:
    if i > 9 or i < 0:
      return "elements are in the range [0, 9]"

  #-->basic variables
  end = len(input_list) - 1

  #--> basic condation
  if end < 1:
    return input_list

  #-->setp 1: sort input list with heap sort
  heapSort(input_list)

  #--> convert elements in input list to string
  arrStr = [str(i) for i in input_list]

  #--> find num1 and num2
  num1 = int("".join(arrStr[end::-2]))
  num2 = int("".join(arrStr[end-1::-2]))

  #--> return with input list
  input_list = [num1] + [num2]

  return input_list

#--> heap sort helper
def heapSort(arr):
  #--> basic variables
  n = len(arr)

  #-->bulding a mini heap
  for i in range(n,-1,-1):
    heapfiy(arr, n, i)
  
  #-->one by one extract elements 
  for i in range(n-1, 0, -1): 
      arr[i], arr[0] = arr[0], arr[i] # swap
      heapfiy(arr, i, 0) 
  
  return arr


#--> bulding a heapfiy helper
def heapfiy(arr, n, index):
  #--> basic variables
  parent        = index
  l_child       = 2 * index + 1
  r_child       = 2 * index + 2

  #-->compare between parent and left child
  if l_child < n and arr[index] < arr[l_child]:
    parent = l_child
  
  #-->compare between parent and right child
  if r_child < n and arr[parent] < arr[r_child]:
    parent = r_child

  #-->if either of left / right child is the largest node
  if parent != index:
    arr[index], arr[parent] = arr[parent], arr[index] 
    heapfiy(arr, n, parent)

print(rearrange_digits([8, 3, 1, 7, 0, 9, 2]))

def rearrange_digits_test():
  test_cases = [#-->Edge cases
                (None, "AssertionError"), #--> return "Assertion Error"
                ([1, 10], "elements are in the range [0, 9]"),#--> elements are in the range [0, 9]
                ([1], [1]),#--> [1]
                ([1, 2], [2, 1]),#--> [2, 1]

                ([1, 2, 3, 4, 5], [531, 42]),#--> return [531, 42]
                ([8, 3, 1, 7, 0, 9, 2], [9720, 831]),#--> return [9720, 831]
                ([4, 6, 2, 5, 9, 8], [964, 852]),#--> return [9720, 831]
               ]

  for arg, answer in test_cases:
    try:
      result  = rearrange_digits(arg)

      if result == answer and answer != "AssertionError":
        print("Test Case is Passed !")
      else:
        print("Test case", arg, "Failed")

    except AssertionError:
      if answer == "AssertionError":
        print("Nice job! Test case {0} correctly raises AssertionError!".format(arg))
      else:
        print("Check your work! Test case {0} should not raise AssertionError!".format(arg))

rearrange_digits_test()