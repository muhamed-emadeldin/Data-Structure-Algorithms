#!/usr/env/bin python

#created Node class
class Node:
  def __init__(self, value):
    self.value = value
    self.next = None

#create a linked list
class LinkedList:
  def __init__(self):
    self.head = None

  def append(self, value):
    if self.head is None:
      self.head = Node(value)
      return
    
    node = self.head

    while node.next:
      node = node.next
    
    node.next = Node(value)

  def __iter__(self):
    node = self.head
    while node:
      yield node.value
      node = node.next

  def __repr__(self):
    return str([v for v in self ])

#create a reverse function in linked list
def reverse(linked_list):
  reverse_list = LinkedList()
  prev_node = None
  for value in linked_list:
    new_node = Node(value)
    new_node.next = prev_node
    prev_node = new_node
  
  reverse_list.head = prev_node
  return reverse_list
  
  

llist= LinkedList()

for val in [4,2,5,1,-3,0]:
  llist.append(val)

flipped = reverse(llist)

print(flipped)