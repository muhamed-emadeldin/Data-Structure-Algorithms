#!/usr/bin/env python

from collections import OrderedDict
class LRU_Cache(object):

    def __init__(self, capacity=None):
        # Initialize class variables
        self.dic = OrderedDict()
        self.num_entries = 0
        self.capacity = capacity

    def get(self, key):
      # Retrieve item from provided key. Return -1 if nonexistent.

      #defense function
      if key is None or key == str(key):
        return None

      #defense function
      
      if self.capacity is None or self.capacity < 1:
        return "capacity should be more than 0"

      #check if key is exsit in dic or no
      if key in self.dic.keys():
        self.dic.move_to_end(key, last=True)
        return self.dic[key]
      return -1

    def set(self, key, value):
      # Set the value if the key is not present in the cache. If the cache is at capacity remove the oldest item. 
      #defense function
      if self.capacity is None or self.capacity < 1:
        return "capacity should be more than 0"

      #check capacity
      if self.capacity == self.num_entries:
        #here I use concept of FIFO
        self.dic.popitem(last=False)
        self.num_entries -= 1

      #put key and value in dictionary and moved to the end of the right
      self.dic[key] = value
      self.dic.move_to_end(key, last=True)
      self.num_entries += 1
      
    # Helper function to see the hashmap
    def __repr__(self):
        output = "\nLet's view the hash map:"
        #defense function
        if self.capacity < 1:
          output = "capacity should be more than 0"

        for key, value in self.dic.items():
          output += '\n[{},{}] '.format(key, value)
       
        return output

#Edge case if capacity < 1
our_cache_1 = LRU_Cache(0)
assert our_cache_1.set(1,1) == "capacity should be more than 0"

#Edge case if capacity is None
our_cache_2 = LRU_Cache()
assert our_cache_2.set(1,1) == "capacity should be more than 0"




our_cache = LRU_Cache(5)
our_cache.set(1, 1)
our_cache.set(2, 2)
our_cache.set(3, 3)
our_cache.set(4, 4)

# function Test
def test_cases_get():
  
  test_cases = [(1, 1), #--> returns 1
                ("1", None), #--> returns None
                (None, None), #--> returns None
                (2, 2), #--> returns 2
                (9, -1), #--> returns -1
                (3, 3), #--> returns 3
               ]
  
  for args, answer in test_cases:
    try:
      result = our_cache.get(args)

      if result == answer and answer != "AssertionError":
        print("Test case get passed!")
      else:
        print("Test with get data:", args, "failed")
    
    except AssertionError:
          if answer == "AssertionError":
              print( "Nice job! Test case {0} correctly raises AssertionError!\n".format(args))
          else:
              print("Check your work! Test case {0} should not raise AssertionError!\n".format(args))

  
test_cases_get()