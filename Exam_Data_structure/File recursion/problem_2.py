#!/usr/bin/env python

'''
Pseudocode:
#--> Check if input path is a dir or file
#--> if path is a dir store it in Queue
#--> check if path is a file and end with suffix
'''

import os

# Create Queue Class
class Queue:
  def __init__(self):
    self.storage = []
  
  def enq(self, value):
    self.storage.append(value)
  
  def deq(self):
    if len(self.storage) > 0:
      return self.storage.pop(0)
  
  def __len__(self):
    return len(self.storage)

  def __str__(self):
    s = ""

    for i in self.storage:
      s += str(i) + " | "
    
    return s


def find_files(suffix, path):
  #defense function
  if path is None or path == "" or not os.path.exists(path):
    return "Please check your path."
  
  if suffix is None or suffix == "":
    return "Please check your suffix."
  
  #basic variables
  out_list = []
  q        = Queue()

  def traversal(suffix, path):
    if os.path.isfile(path):
      if path.endswith(suffix):
        out_list.append(path)
    
    elif os.path.isdir(path):   
      for pth in os.listdir(path):
        new_path = os.path.join(path, pth)
        q.enq(new_path)

    while len(q) >= 1:
      first = q.deq()
      traversal(suffix, first)
  
  traversal(suffix, path)


  if len(out_list) > 0:
    return out_list
  
  return None



# Test Function with 5 cases 
def test():
  
  test_cases = [#Test 1 --> Edge case if a path is not exists
                ((".c", ""), ("Please check your path.")),
                
                #Test 2 --> Edge case if a suffix is not exists
                (("", "File recursion/testdir/"), "Please check your suffix."),

                #Test 3 --> Edge case if a suffix and path are not exist
                (("", ""), "Please check your path."),

                #Test 4 --> if inputs as an example
                ((".c", "File recursion/testdir/"), ['File recursion/testdir/t1.c', 'File recursion/testdir/subdir1/a.c', 'File recursion/testdir/subdir5/a.c', 'File recursion/testdir/subdir3/subsubdir1/b.c']),

                #Test 5 --> if change suffix to .h
                ((".h", "File recursion/testdir/"), ['File recursion/testdir/t1.h', 'File recursion/testdir/subdir1/a.h', 'File recursion/testdir/subdir5/a.h', 'File recursion/testdir/subdir3/subsubdir1/b.h']),

                #Test 6 --> if path is file
                ((".py", "File recursion/problem_2.py"), ['File recursion/problem_2.py']),

                #Test 7 --> if change suffix to .py
                ((".py", "File recursion/testdir/"), None),
               ]
  
  for (args, answer) in test_cases:
      try:
          result = find_files(*args)
          if result == answer and answer != "AssertionError":
              print("Test case file passed!")
          else:
              print("Test with data:", args, "failed")
  
      except AssertionError:
          if answer == "AssertionError":
              print( "Nice job! Test case {0} correctly raises AssertionError!\n".format(args))
          else:
              print("Check your work! Test case {0} should not raise AssertionError!\n".format(args))          
test()
