#!/usr/bin/env python

def contains(target, source):
  #defense function
  if source is None or len(source) == 0:
    return source
  
  if not isinstance(target, str):
    return target
  
  #basic variables
  right = 0
  left = len(source) - 1

  while right <= left:
    midd = (left + right) // 2
    if source[midd] == target:
      return True
    elif source[midd] < target:
      right = midd + 1
    else:
      left = midd - 1
  
  return False

letters = ['a', 'c', 'd', 'f', 'g']
print(contains('b', letters)) ## False

def test_case():
  test_cases=[(("a", ['a', 'c', 'd', 'f', 'g']),True),
              (("b", ['a', 'c', 'd', 'f', 'g']),False),
              (("b", None),None),
              ((None, ['a', 'c', 'd', 'f', 'g']),None),
             ]
  try:
    for (args, answer) in test_cases:
      result = contains(*args)
      if result == answer and answer != "AssertionError":
        print("Test case contain passed!")
      else:
        print("Test with data", *args, "faild")
  
  except AssertionError:
    if answer == "AssertionError":
      print( "Nice job! Test case {0} correctly raises AssertionError!\n".format(args))
    else:
      print("Check your work! Test case {0} should not raise AssertionError!\n".format(args))

test_case()
