#!/usr/bin/env python 3.8

'''
We implemnt a Mini heap with using:
  - Complete Binary Tree
  - Heap order property
'''

class MiniHeap:
  def __init__(self, capacity):
    self.arr = [None for _ in range(capacity)]
    self.next_index = 0

  def insert(self, data):
    self.arr[self.next_index] = data
    self.up_heapfiy()
    self.next_index += 1

    #increase capacity if next_index > capacity
    if self.next_index > len(self.arr):
      temp = self.arr
      self.arr = [None for _ in range(2*len(temp))]
      for i in range(len(temp)):
        self.arr[i] = temp[i]


  def remove(self):
    if self.is_empty():
      return None
    
    self.next_index -= 1
    to_remove        = self.arr[0]
    last_element     = self.arr[self.next_index]

    self.arr[0] = last_element
    self.arr[self.next_index] = to_remove
    self.down_heapfiy()

    return to_remove




  def down_heapfiy(self):
    parent_index = 0

    while parent_index < self.next_index:
        left_child_index = 2 * parent_index + 1
        right_child_index = 2 * parent_index + 2

        parent = self.arr[parent_index]
        left_child = None
        right_child = None

        min_element = parent

        # check if left child exists
        if left_child_index < self.next_index:
            left_child = self.arr[left_child_index]

        # check if right child exists
        if right_child_index < self.next_index:
            right_child = self.arr[right_child_index]

        # compare with left child
        if left_child is not None:
            min_element = min(parent, left_child)

        # compare with right child
        if right_child is not None:
            min_element = min(right_child, min_element)

        # check if parent is rightly placed
        if min_element == parent:
            return

        if min_element == left_child:
            self.arr[left_child_index] = parent
            self.arr[parent_index] = min_element
            parent = left_child_index

        elif min_element == right_child:
            self.arr[right_child_index] = parent
            self.arr[parent_index] = min_element
            parent = right_child_index


  def up_heapfiy(self):
    child_index = self.next_index

    while child_index >= 1:
      parent_index  = (child_index - 1) // 2
      parent        = self.arr[parent_index]
      child         = self.arr[child_index]

      if parent > child:
        self.arr[parent_index]  = child
        self.arr[child_index]   = parent
        child_index = parent_index
      
      else:
        break

  def front(self):
    return self.arr[0]
  
  def size(self):
    return self.next_index

  def is_empty(self):
    return self.next_index == 0

  def __str__(self):
    return " ".join([str(i) for i in self.arr])


heap = MiniHeap(2)
heap.insert(10)
heap.insert(9)
# heap.insert(3)
# heap.insert(2)
# heap.insert(1)
print(heap.front())
print(heap)