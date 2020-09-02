#!/usr/bin/env python

def count_inversions(arr):
  if len(arr) <= 1:
    return 0

  inv = 0
  for i in range(len(arr)):
    for x in range(1,len(arr)):
      curr = arr[x]
      prev = arr[x-1]
      if curr < prev:
        arr[x] = prev
        arr[x-1] = curr
        inv += 1
  return inv
  
def test_merged_sort():
  test_case = [
                ([0,1], 0),
                ([2, 1], 1),
                ([3,1,2,4], 2),
                ([2, 5, 1, 3, 4], 4),
                ([54, 99, 49, 22, 37, 18, 22, 90, 86, 33], 26),
                ([1, 2, 4, 2, 3, 11, 22, 99, 108, 389], 2),
              ]

  for args, answer in test_case:
    try:
      result = count_inversions(args)
      if result == answer and answer != "AssertionError":
        print("Test Case is Passed!!!")
      
      else:
        print("Test Case", args, "Faild")
    except AssertionError:
      pass

test_merged_sort()