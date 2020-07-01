'''
Exercise 1 - Implementing a simple linked list
'''

class Node:
  def __init__(self, value):
    self.value = value
    self.next = None

class LinkedList:
  def __init__(self):
    self.head = None

  
  def append(self, value):
    if self.head is None:
      self.head = Node(value)
      return

    node = self.head
    while node.next:
      node      = node.next

    node.next = Node(value)

    return

  def to_list(self):
    out_list = []
    node = self.head
    while node:
      out_list.append(node.value)
      node = node.next
    return out_list

linked_list = LinkedList()
linked_list.append(1)
linked_list.append(2)
linked_list.append(4)

node = linked_list.head
while node:
  print(node.value)
  node = node.next

linked_list.to_list()