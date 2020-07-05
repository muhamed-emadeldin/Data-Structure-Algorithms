#!/usr/bin/env python

"""
Reversed Queue
Write a function that takes a queue as an input and returns a reversed version of it.
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
      new_node.next = new_node
      self.head = new_node.next
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
    return self.head.data


#create Queue Class
class Queue:
  def __init__(self):
    self.head = None
    self.tail = None
    self.queue_size = 0

  def enqueue(self, data):
    new_node = Node(data)
    if self.head is None:
      self.head = new_node
      self.tail = self.head

    else:
      self.tail.next = new_node
      self.tail = self.tail.next
    
    self.queue_size += 1

  def dequeue(self):
    if self.is_empty():
      return None

    value = self.head.data
    self.head = self.head.next
    self.queue_size -= 1
    return value

  def is_empty(self):
    return self.queue_size == 0

  def size(self):
    return self.queue_size

def reverse_queue(queue):
    """
    Reverese the input queue

    Args:
       queue(queue),str2(string): Queue to be reversed
    Returns:
       queue: Reveresed queue
    """
    
    # TODO: Write reversed queue function
    #basic variables
    stack = Stack()
    new_queue = Queue()
    #defense function
    if queue is None:
      return None

    while not queue.is_empty():
      stack.push(queue.dequeue())
    
    while not stack.is_empty():
      new_queue.enqueue(stack.pop())

    return new_queue


    
  

    


    


def test_function(test_case):
    queue = Queue()
    for num in test_case:
        queue.enqueue(num)
    
    reverse_queue(queue)
    index = len(test_case) - 1
    while not queue.is_empty():
        removed = queue.dequeue()
        if removed != test_case[index]:
            print("Fail")
            return
        else:
            index -= 1
    print("Pass")

test_case_1 = [1, 2, 3, 4]
test_function(test_case_1)

test_case_2 = [1]
test_function(test_case_2)

test_case_2 = [5,3]
test_function(test_case_2)