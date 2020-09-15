#!/usr/bin/env python

def rotated_array_search(input_list, number):
  #-->defense function
  assert(isinstance(input_list, list)), "AssertionError"
  assert(isinstance(number, int)), "AssertionError"

  n               = len(input_list)
  pivot           = findPivot(input_list, 0, n-1)

  #--> defense function (if we didn't found pivot)
  if pivot == -1:
    return binary_search_tree(input_list, number, 0, n-1)

  #--> basic variables
  p_index         = input_list.index(pivot)
  left            = input_list[:p_index]
  right           = input_list[p_index+1:]
  
  #--> cases to found target number
  if number == pivot:
    return p_index
  elif number > right[-1]:
    return binary_search_tree(left, number, 0, (len(left) - 1))
  else:
    return binary_search_tree(right, number, 0, (len(right) - 1)) + p_index + 1

#--> findPivot helper function
def findPivot(arr, start, end):
  #-->basic variables
  midd = (start + end) // 2
  midd_elm = arr[midd]

  #-->basic condation
  if start > end or (midd + 1) >= len(arr):
    return -1

  prev_elm  = arr[midd - 1]
  next_elm  = arr[midd + 1]

  #-->get a good pivot
  if midd_elm > prev_elm and midd_elm > next_elm:
    return midd_elm
  elif midd_elm < prev_elm:
    return findPivot(arr, start, midd - 1)
  else:
    return findPivot(arr, midd + 1, end)


#--> binary search helper
def binary_search_tree(arr, target, start, end):
  if start > end:
    return -1
  
  midd = (start + end) // 2

  if arr[midd] == target:
    return midd

  elif arr[midd] > target:
    return binary_search_tree(arr, target, start, midd - 1)

  else:
    return binary_search_tree(arr, target, midd + 1, end)


def rotated_array_search_test():
  test_cases = [#-->Edge cases
                ((None, 8), "AssertionError"), #--> return "Assertion Error"
                (([6, 7, 8, 9, 10, 1, 2], None), "AssertionError"), #--> return "Assertion Error"
                (([0, 1, 2, 3, 8, 9, 10], 8), 4), #--> return 4 if list is non rotated but sorted

                (([6, 7, 8, 9, 10, 1, 2, 3, 4], 8), 2), #--> return 2
                (([6, 7, 8, 9, 10, 1, 2, 3, 4], 1), 5),#--> return 5
                (([6, 7, 8, 1, 2, 3, 4], 8), 2),#--> return 2
                (([6, 7, 8, 1, 2, 3, 4], 1), 3),#--> return 3
                (([6, 7, 8, 1, 2, 3, 4], 10), -1),#--> return -1
               ]

  for (args, answer) in test_cases:
    try:
      result  = rotated_array_search(*args)

      if result == answer and answer != "AssertionError":
        print("Test Case is Passed !")
      else:
        print("Test case", args, "Failed")

    except AssertionError:
      if answer == "AssertionError":
        print("Nice job! Test case {0} correctly raises AssertionError!".format(args))
      else:
        print("Check your work! Test case {0} should not raise AssertionError!".format(args))

rotated_array_search_test()



  