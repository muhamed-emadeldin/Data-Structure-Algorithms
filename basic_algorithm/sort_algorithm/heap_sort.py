#!/usr/bin/env python

def heap_sort(arr):
  #-->basic variables
  n = len(arr)
  #--build a max heap
  for i in range(n,-1,-1):
    heapfiy(arr, n, i)
  #-->one by one extract elements 
  for i in range(n-1, 0, -1): 
      arr[i], arr[0] = arr[0], arr[i] # swap
      heapfiy(arr, i, 0) 
  
  return arr

def heapfiy(arr, n, i):
  parent_index  = i
  left_child    = 2 * i + 1
  right_child   = 2 * i + 2

  #-->compare with left child
  if left_child < n and arr[i] < arr[left_child]:
    parent_index = left_child
  
  #-->compare with right child
  if right_child < n and arr[parent_index] < arr[right_child]:
    parent_index = right_child
  
  #-->if either of left / right child is the largest node
  if parent_index != i:
    arr[i], arr[parent_index] = arr[parent_index], arr[i] 
    heapfiy(arr, n, parent_index)
  
  
  



 

def test_heap_sort():
  test_case = [
                ([3, 7, 4, 6, 1, 0, 9, 8, 9, 4, 3, 5], [0, 1, 3, 3, 4, 4, 5, 6, 7, 8, 9, 9]),
                ([8, 3, 1, 7, 0, 10, 2], [0, 1, 2, 3, 7, 8, 10]),
                ([1, 0], [0, 1]),
              ]

  for args, answer in test_case:
    try:
      result = heap_sort(args)
      if result == answer and answer != "AssertionError":
        print("Test Case is Passed!!!")
      
      else:
        print("Test Case", args, "Faild")
    except AssertionError:
      pass

test_heap_sort()