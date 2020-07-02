#!/usr/bin/env python

"""
Reverse Polish notation, also referred to as Polish postfix notation is a way of laying out operators and operands.
When making mathematical expressions, we typically put arithmetic operators (like +, -, *, and /) between operands. For example: 5 + 7 - 3 * 8
However, in Reverse Polish Notation, the operators come after the operands. For example: 3 1 + 4 *
The above expression would be evaluated as (3 + 1) * 4 = 16
The goal of this exercise is to create a function that does the following:
Given a postfix expression as input, evaluate and return the correct final answer.
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

  def push(self, item):
    new_node = Node(item)

    if self.head is None:
      self.head = new_node
    
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
    return self.num_elements == 0



def evaluate_post_fix(input_list):
    """
    Evaluate the postfix expression to find the answer

    Args:
       input_list(list): List containing the postfix expression
    Returns:
       int: Postfix expression solution
    """
    #basic variables
    stack = Stack()
    oprts = ["*", "+", "-", "/", "%"]
    result = None
    temp1 = None
    temp2 = None
    # TODO: Iterate over elements
    # defense function
    if input_list is None:
      return None

    for char in input_list:
      #check if char is +, - *, ...
      if not char in oprts:
        stack.push(char)
      
      else:
        temp1 = stack.pop()
        temp2 = stack.pop()

        if temp1 is not None and temp2 is not None:
          if char == "/":
            result = eval(str(temp2) + char + str(temp1))
            if result < 1:
              stack.push(1)
            stack.push(int(result))
          
          else:
            result = eval(str(temp2) + char + str(temp1))
            stack.push(result)

    return stack.pop()


def test_function(test_case):
    output = evaluate_post_fix(test_case[0])
    print(output)
    if output == test_case[1]:
        print("Pass")
    else:
        print("Fail")

test_case_1 = [["3", "1", "+", "4", "*"], 16]
test_function(test_case_1)

test_case_2 = [["4", "13", "5", "/", "+"], 6]
test_function(test_case_2)


test_case_3 = [["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"], 22]
test_function(test_case_3)