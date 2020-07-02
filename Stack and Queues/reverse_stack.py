#!/usr/bin/env python

"""
Reverse a stack. If your stack initially has 1, 2, 3, 4 (4 at the top and 1 at the bottom), after reversing the order must be 4, 3, 2, 1 (4 at the bottom and 1 at the top).
"""

#create Node Class
class Node:
  def __init__(self, data):
    self.data = data
    self.next = None

#create Stack Class
class Stack:
  def __init__(self):
    self.head = None
    self.num_elements = 0

  def push(self, data):
    new_node = Node(data)

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

  def size(self):
    return self.num_elements

  def is_empty(self):
    return self.num_elements ==0


def reverse_stack(stack):
    """
    Reverse a given input stack

    Args:
       stack(stack): Input stack to be reversed
    Returns:
       stack: Reversed Stack
    """
    
    # TODO: Write the reverse stack function
      
    #basic variables
    new_list = []

    #defense function
    if stack.size() <= 1:
      return stack

    while stack.head is not None:
      new_list.append(stack.pop())

    for _ in new_list:
      stack.push(_)

    return stack


def test_function(test_case):
    stack = Stack()
    for num in test_case:
        stack.push(num)
    
    reverse_stack(stack)
    index = 0
    while not stack.is_empty():
        popped = stack.pop()
        if popped != test_case[index]:
            print("Fail")
            return
        else:
            index += 1
    print("Pass")


test_case_1 = [1, 2, 3, 4]
test_function(test_case_1)

test_case_2 = [1]
test_function(test_case_2)