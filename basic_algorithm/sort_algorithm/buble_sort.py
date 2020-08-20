#!/usr/bin/env python
def buble_sort(arr):
  for i in range(len(arr)):
    for item in range(1, len(arr)):
      first = arr[item -1]
      second = arr[item]

      if first <= second:
        continue

      arr[item-1] = second
      arr[item]   = first
  return arr

def buble_sort_2(cbt):
  for i in range(len(cbt)):
    for tup in range(1, len(cbt)):
      this = cbt[tup]
      prev = cbt[tup - 1]

      if prev >= this:
        continue

      cbt[tup]    = prev
      cbt[tup -1] = this

  return cbt 

def test_buble_sort():
  test_cases = [
                ([16,49,3,12,56,49,55,22,13,46,19,55,46,13,25,56,9,48,45], [3, 9, 12, 13, 13, 16, 19, 22, 25, 45, 46, 46, 48, 49, 49, 55, 55, 56, 56]),

                ([8, 5, 1, 3, 4, 0], [0, 1, 3, 4, 5, 8]),
               ]

  try:
    for args, answer in test_cases:
      result = buble_sort(args)
      if result == answer and answer != "AssertionError":
        print("Test Case is Passed")
      
      else:
        print("Test Case", args, "Faild")


  except AssertionError:
    pass

test_buble_sort()


def test_buble_sort_2():
  test_case = [([(1, 2), (5,3)], [(5, 3), (1,2)]),
                ([(24,13), (21,55), (23,20), (22,5), (24,23), (21,58), (24,3)], [(24,23), (24,13), (24,3), (23,20), (22,5), (21,58), (21,55)])
              ]

  for args, answer in test_case:
    try:
      result = buble_sort_2(args)
      if result == answer and answer != "AssertionError":
        print("Test Case Passed!")
      else:
        print("Test Case", args, "Faild")
    except AssertionError:
      pass

test_buble_sort_2()