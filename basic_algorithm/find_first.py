#!/usr/bin/env python

def recursive_binary_search(target, source, right = 0):
  if len(source) == 0:
    return source
  
  midd = (len(source)-1) // 2

  if source[midd] == target:
    return midd + right
  
  elif target > source[midd]:
    return recursive_binary_search(target, source[midd+1:], right=right+midd+1)
  else:
    return recursive_binary_search(target, source[:midd], right)

def find_first(target, source):
    #defense function
    index = recursive_binary_search(target, source)

    if not index:
      return None
    
    while source[index] == target:
      if index == 0:
        return 0
      elif source[index-1] == target:
        index -= 1
      else:
        return index
    
        

multiple = [1, 3, 5, 7, 7, 7, 8, 11, 12, 13, 15, 15]
print(find_first(7, multiple)) # Should return 3
print(find_first(9, multiple)) # Should return None
print(find_first(15, multiple)) # Should return 11