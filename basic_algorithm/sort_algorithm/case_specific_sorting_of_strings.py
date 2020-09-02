#!/usr/bin/env python

def case_sort(string):
  assert(isinstance(string, str)), "AssertionError"
  assert(string.isalpha()), "AssertionError"
  #--basic variable
  out_lower = []
  out_upper = []
  out_string = ""

  #-->split string to out_lower array and out_upper array
  for chr in string:
    if chr.islower():
      out_lower.append(chr)
    else:
      out_upper.append(chr)

  #-->sort out_lower array and out_upper array with buble sort O(n^2)
  out_lower = buble_sort(out_lower)
  out_upper = buble_sort(out_upper)

  #--> pick lower case and upper case character in out string
  while len(out_lower) >= 1 and len(out_upper) >= 1:
    for chr in string:
      if chr.islower():
        out_string += out_lower.pop(0)
      else:
        out_string += out_upper.pop(0)

  return out_string

def buble_sort(arr):
  for i in range(len(arr)):
    for j in range(1,len(arr)):
      prev = arr[j-1]
      curr = arr[j]

      if prev > curr:
        arr[j-1] = curr
        arr[j]    = prev
  
  return arr

def test_case_sort():
  test_cases = [
                #-->Edge Case
                ("555555555555", "AssertionError"),
                (555555555555, "AssertionError"),
                ("fedRTSersUXJ", "deeJRSfrsTUX"),
                ("defRTSersUXI", "deeIRSfrsTUX"),
                ("earQSCeryYZX", "aeeCQSrryXYZ"),
               ]

  for arg, answer in test_cases:
    try:
      result = case_sort(arg)
      if result == answer and answer != "AssertionError":
        print("Test Case Passed !")
      else:
        print("Test Case", arg, "Faild")
    except AssertionError:
      print( "Nice job! Test case {0} correctly raises AssertionError!".format(arg))

test_case_sort()