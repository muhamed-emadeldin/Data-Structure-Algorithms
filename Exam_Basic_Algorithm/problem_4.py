#!/usr/bin/env python

def sort_012(input_list):
  #-->defense function
  assert(isinstance(input_list, list)), "AssertionError"

  #--basic condation
  n     = len(input_list)
  new_list  = [None] * n

  start = 0
  end   = -1
  for item in input_list:
    #-->defense function
    assert(isinstance(item, int)), "AssertionError"
    if item >= 0 and item <=2:
      if item == 0:
        new_list[start] = 0
        start += 1
      elif item == 2:
        new_list[end] = 2
        end -= 1
    else:
      return "numbers should be between 0-2"

  
  new_list[start:end+1] = [1]*len(new_list[start:end+1])

  return new_list

  
  
def sort_012_test():
  test_cases = [#-->Edge cases
                (None, "AssertionError"), #--> return "Assertion Error"
                ([2, 1, 0, 0, 0, "2"], "AssertionError"), #--> return "Assertion Error"
                ([2, 1, 3, 0, 0, 2], "numbers should be between 0-2"), #--> return "Assertion Error"

                ([0, 0, 2, 2, 2, 1, 1, 1, 2, 0, 2], [0, 0, 0, 1, 1, 1, 2, 2, 2, 2, 2]),#--> return [0, 0, 0, 1, 1, 1, 2, 2, 2, 2, 2]

                ([2, 1, 2, 0, 0, 2, 1, 0, 1, 0, 0, 2, 2, 2, 1, 2, 0, 0, 0, 2, 1, 0, 2, 0, 0, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2]),#--> return [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2]

                ([0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2], [0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2]),#--> return [0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2]
                
               ]

  for arg, answer in test_cases:
    try:
      result  = sort_012(arg)

      if result == answer and answer != "AssertionError":
        print("Test Case is Passed !")
      else:
        print("Test case", arg, "Failed")

    except AssertionError:
      if answer == "AssertionError":
        print("Nice job! Test case {0} correctly raises AssertionError!".format(arg))
      else:
        print("Check your work! Test case {0} should not raise AssertionError!".format(arg))

sort_012_test()

