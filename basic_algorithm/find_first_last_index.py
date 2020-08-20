#!/usr/bin/env python

def binary_search(arr, target, l, r):
  if r >= l:
    midd = (l+r) // 2
    if arr[midd] == target:
      return midd
    elif arr[midd] < target:
      return binary_search(arr, target, midd+1, r)
    else:
      return binary_search(arr, target, l, r=midd - 1)
  else:
    return -1

def first_and_last_index(arr, number):
  #defense function
  assert (isinstance(arr, list)), "AssertionError"
  assert (isinstance(number, int)), "AssertionError"

  #basic variables
  out = [-1, -1]
  Index = binary_search(arr, number, 0, len(arr)-1)

  #if we not found target in arr
  if Index == -1:
    return out

  # search first occurence
  if arr[Index] == number:
    #check if the right value center contains target
    while (Index -1) > 0 and arr[Index - 1] == number:
      Index = binary_search(arr, number, 0, Index-1)
    out[0] = Index
    #check if the left elements of midd contains target
    while (Index +1) < len(arr) and arr[Index + 1] == number:
      Index = binary_search(arr, number, Index+1, len(arr)-1)
    out[-1] = Index

  return out

def test_first_last_index():
  test_cases = [(([1],1), [0,0]),
                (([1, 2, 2] ,2), [1,2]),
                (([0, 1, 2, 3, 3, 3, 3, 4, 5, 6],3), [3,6]),
                (([0, 1, 2, 3, 4, 5],5), [5,5]),
                (([0, 1, 2, 3, 4, 5],6), [-1,-1]),
                (([5, 5, 5, 5, 5, 5], 5), [0,5]),
                (([0, 1, 2, 3, 4, 5],None), "AssertionError"),
                ((None,2), "AssertionError"),
               ]

  try:
    for (args, answer) in test_cases:
      result = first_and_last_index(*args)
      if result == answer and answer != "AssertionError":
        print("Test case index passed!")
      else:
        print("Test case data", args, "faild")
  except AssertionError:
    if answer == "AssertionError":
      print( "Nice job! Test case {0} correctly raises AssertionError!\n".format(args))
    else:
      print("Check your work! Test case {0} should not raise AssertionError!\n".format(args))

test_first_last_index()