#!/usr/bin/env python

def merge_sorted(items):
  #--> basic variables
  if len(items) <= 1:
    return items

  midd = len(items) //2
  left = items[:midd]
  right = items[midd:]

  left = merge_sorted(left)
  right = merge_sorted(right)

  return merge(left, right)

def merge(left, right):
  #--> basic variables
  merged = []
  left_index = 0
  right_index = 0

  while left_index < len(left) and right_index < len(right):
    if left[left_index] < right[right_index]:
      merged.append(left[left_index])
      left_index += 1

    else:
      merged.append(right[right_index])
      right_index += 1

  merged += left[left_index:]
  merged += right[right_index:]

  return merged



def test_merged_sort():
  test_case = [
                ([5,3,2,1], [1, 2, 3, 5]),
                ([8, 3, 1, 7, 0, 10, 2], [0, 1, 2, 3, 7, 8, 10]),
                ([1, 0], [0, 1]),
              ]

  for args, answer in test_case:
    try:
      result = merge_sorted(args)
      if result == answer and answer != "AssertionError":
        print("Test Case is Passed!!!")
      
      else:
        print("Test Case", args, "Faild")
    except AssertionError:
      pass

test_merged_sort()