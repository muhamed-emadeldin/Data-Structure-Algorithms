#!/usr/bin/en python
"""
Given an input string consisting of only { and }, figure out the minimum number of reversals required to make the brackets balanced.

For example:

For input_string = "}}}}, the number of reversals required is 2.
For input_string = "}{}}, the number of reversals required is 1.
"""

#create Node Class
class Node:
  def __init__(self, data):
    self.data = data
    self.next = None

#create Stack class
class Stack:
  def __init__(self):
    self.head = None
    self.num_elements = 0

  def push(self, value):
    new_node = Node(value)

    if self.head is None:
      self.head = new_node

    else:
      new_node.next = self.head
      self.head = new_node
    self.num_elements += 1

  def pop(self):
    if self.is_empty():
      return None
    
    value = self.head.data
    self.head = self.head.next
    self.num_elements -= 1
    return value

  def is_empty(self):
    return self.num_elements == 0

  def size(self):
    return self.num_elements

  def top(self):
    if self.head is None:
      return None
    return self.head.data


def minimum_bracket_reversals(input_string):
    """
    Calculate the number of reversals to fix the brackets

    Args:
       input_string(string): Strings to be used for bracket reversal calculation
    Returns:
       int: Number of breacket reversals needed
    """
    
    # TODO: Write function here
    
    #defense function
    if input_string is None:
      return input_string
    
    #brackets cannot be balanced
    if len(input_string) % 2 != 0:
      return -1

    #basic variables
    stack = Stack()
    ls = []
    cont = 0
    for char in input_string:
      
      if stack.is_empty():
        stack.push(char)
      
      else:
        top = stack.top()
        if top != char:
          print("not Equal")
          if top == "{":
            stack.pop()
            continue
        stack.push(char)
          
    while not stack.is_empty():
      first = stack.pop()
      second = stack.pop()
      ls.append(first)
      ls.append(second)

      if first == "}" and second == "}":
        cont += 1
      elif first == "{" and second == "}":
        cont += 2
      elif first == "{" and second == "{":
        cont += 1
    print(cont)
    return cont

def test_function(test_case):
    input_string = test_case[0]
    expected_output = test_case[1]
    output = minimum_bracket_reversals(input_string)
    
    if output == expected_output:
        print("Pass")
    else:
        print("Fail")

test_case_1 = ["}}}}", 2]
test_function(test_case_1)

test_case_2 = ["}}{{", 2]          
test_function(test_case_2)