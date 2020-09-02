#!/usr/bin/env python

def pair_sum(arr, target):
  arr = merge_sort(arr)
  front_index = 0
  last_index  = len(arr) - 1

  while front_index < last_index:
    front = arr[front_index]
    back = arr[last_index]

    if front + back == target:
      return [front, back]
    elif front + back < target:
      front_index += 1
    else:
      last_index -= 1
  
  return [None]*2

def merge_sort(arr):
  if len(arr) <= 1:
    return arr

  midd = len(arr) // 2
  left  = arr[:midd]
  right = arr[midd:]

  left = merge_sort(left)
  right = merge_sort(right)

  return merge(left, right)

def merge(left, right):
  merged = []
  left_index = 0
  right_index = 0

  while left_index < len(left) and right_index < len(right):

    if left[left_index] > right[right_index]:
      merged.append(right[right_index])
      right_index += 1
    else:
      merged.append(left[left_index])
      left_index += 1


  merged += left[left_index:]
  merged += right[right_index:]

  return merged



def test_merged_sort():
  test_case = [
                (([2, 7, 11, 15], 9), [2, 7]),
                (([0, 8, 5, 7, 9], 9), [0, 9]),
                (([110, 9, 89], 9), [None, None]),
              ]

  for (args, answer) in test_case:
    try:
      result = pair_sum(*args)
      if result == answer and answer != "AssertionError":
        print("Test Case is Passed!!!")
      
      else:
        print("Test Case", *args, "Faild")
    except AssertionError:
      pass

test_merged_sort()

