#!/usr/bin/env python

def get_min_max(arr):
  #-->defense function
  assert(isinstance(arr, list)), "AssertionError"
  #-->basic condation
  if len(arr) <= 1:
    return arr

  #-->basic variable
  min_elm = arr[0]
  max_elm = arr[0]

  #-->loop in array
  for num in arr:
    if num > max_elm:
      max_elm = num
    elif num < min_elm:
      min_elm = num
  return min_elm, max_elm
  
def get_min_max_test():
  test_cases = [#-->Edge cases
                (None, "AssertionError"), #--> return "Assertion Error"
                ([-1], [-1]), #--> return [-1]
                ([-1, 0], (-1, 0)), #--> return [-1]


                ([6, 7, 8, 9, 10, 1, 2], (1, 10)),#--> return (1, 10)
                ([6, 7, 8, 1, 2, 3, 4], (1, 8)),#--> return (1, 8)
                ([0, 9], (0, 9)),#--> return (0, 9)
                ([5, 4, 3, 2, 1, 0, 7, 8, 6, 9], (0, 9)),#--> return (0, 9)s
               ]

  for arg, answer in test_cases:
    try:
      result  = get_min_max(arg)
      if result == answer and answer != "AssertionError":
        print("Test Case is Passed !")
      else:
        print("Test case", arg, "Failed")

    except AssertionError:
      if answer == "AssertionError":
        print("Nice job! Test case {0} correctly raises AssertionError!".format(arg))
      else:
        print("Check your work! Test case {0} should not raise AssertionError!".format(arg))

get_min_max_test()