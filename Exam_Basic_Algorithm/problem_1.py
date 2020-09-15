#!/usr/bin/env python

def sqrt(number):
  #-->defense function
  assert(isinstance(number, int)), "AssertionError"
  assert(number >= 0), "AssertionError"

  #-->basic cases
  if number == 0 or number == 1:
    return number

  #-->basic variables
  start = 2
  end   = number - 1

  return binary_search(number, start, end)

#--> binary search helper
def binary_search(target, start, end):
  #-->find pivot
  midd = (start + end) // 2

  #-->basic condation
  if start > end:
    return midd

  if (midd ** 2) == target:
    return midd
  elif (midd ** 2) > target:
    return binary_search(target, start, midd - 1)
  else:
    return binary_search(target, midd + 1, end)


def sqrt_test():
  test_cases = [#-->Edge cases
                (None, "AssertionError"), #--> return "Assertion Error"
                (-1, "AssertionError"), #--> return "Assertion Error"
                ("4", "AssertionError"), #--> return "Assertion Error"

                (0, 0),#--> return 0
                (1, 1),#--> return 1
                (2, 1),#--> return 1
                (4, 2),#--> return 2
                (16, 4),#--> return 4
                (36, 6),#--> return 6
                (27, 5),#--> return 0
                (9, 3),#--> return 3

               ]

  for arg, answer in test_cases:
    try:
      result  = sqrt(arg)
      if result == answer and answer != "AssertionError":
        print("Test Case is Passed !")
      else:
        print("Test case", arg, "Failed")

    except AssertionError:
      if answer == "AssertionError":
        print("Nice job! Test case {0} correctly raises AssertionError!".format(arg))
      else:
        print("Check your work! Test case {0} should not raise AssertionError!".format(arg))

sqrt_test()