#!/usr/bin/env python


def count_inversion(ls): #--> Time Complixty O(n)
  #-->basic vriables
  inversion = 0
  #--> get middle
  midd = len(ls) //2
  #--> divied array to left and right
  left = ls[:midd]
  right = ls[midd:]

  #-->sort left array and right array
  left, inv_l = buble_sort(left, inversion)
  right, inv_r = buble_sort(right, inversion)

  #--> compare between each of item in left array and rigth array
  merge, count = compare_sort_left_right_array(left, right, inversion)
  inversion += inv_l + inv_r + count

  return inversion

def buble_sort(ls, inversion):
  for i in range(len(ls)):#--> Time Complixty O(n^2)
    for j in range(1, len(ls)):
      prev = ls[j-1]
      curr = ls[j]

      if prev > curr:
        ls[j-1] = curr
        ls[j]   = prev
        inversion += 1
  return ls, inversion

def compare_sort_left_right_array(left, right, inversion):
  #-->basic variables
  merged = []
  left_index = 0
  right_index = 0
  
  while left_index < len(left) and right_index < len(right): #--Time Complixty O(n)
    if left[left_index] > right[right_index]:
      merged.append(right[right_index])
      inversion += len(left[left_index:])
      right_index += 1
    
    else:
      merged.append(left[left_index])
      left_index += 1

  merged += left[left_index:]
  merged += right[right_index:]

  return merged, inversion

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
      result = count_inversion(args)
      if result == answer and answer != "AssertionError":
        print("Test Case is Passed!!!")
      
      else:
        print("Test Case", args, "Faild")
    except AssertionError:
      pass

test_merged_sort()