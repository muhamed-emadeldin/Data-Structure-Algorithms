#!/usr/bin/env python

"""
In this exercise you are going to apply what you learned about stacks with a real world problem. We will be using stacks to make sure the parentheses are balanced in mathematical expressions such as:  ((32+8)∗(5/2))/(2+6).  In real life you can see this extend to many things such as text editor plugins and interactive development environments for all sorts of bracket completion checks.

Take a string as an input and return True if it's parentheses are balanced or False if it is not.
"""

class Stack:
  #create initial defenation
  def __init__(self):
    self.items = []

  #create size defenation
  def size(self):
    return len(self.items)

  #create push defenation
  def push(self, item):
    self.items.append(item)

  #create pop defenasion
  def pop(self):
    if self.size() == 0:
      return None
    return self.items.pop()


def equation_checker(equation):
    """
    Check equation for balanced parentheses

    Args:
       equation(string): String form of equation
    Returns:
       bool: Return if parentheses are balanced or not
    """
    
    
    # TODO: Intiate stack object
    new_list = Stack()
    
    # TODO: Interate through equation checking parentheses
    for char in equation:
      if char == "(":
        new_list.push(char)
      elif char == ")":
        if new_list.pop() == None:
          return False
    # TODO: Return True if balanced and False if not
    
    if new_list.size() == 0:
      return True
    
    return False

print(equation_checker("((3^2 + 8)*(5/2))/(2+6)"))
print(equation_checker("((3^2 + 8)*(5/2))/(2+6))"))
