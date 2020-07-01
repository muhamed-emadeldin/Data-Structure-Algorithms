#!/usr/bin/env python

"""
Problem Statement
Given a linked list with integer data, arrange the elements in such a manner that all nodes with even numbers are placed after odd numbers. Do not create any new nodes and avoid using any other data structure. The relative order of even and odd elements must not change.
"""

#create class node
class Node:
  def __init__(self, dataval=None):
    self.data = dataval
    self.next = None


def even_after_odd(head):
    """
    :param - head - head of linked list
    return - updated list with all even elements are odd elements
    """
    #defense condation
    if head is None:
        return head

    #basic variables
    even_head = None
    even_tail = None

    odd_head = None
    odd_tail = None

    current = head

    while current is not None:
      node_next = current.next

      if current.data % 2 == 0:
        if even_head is None:
          even_head = current
          even_tail = even_head
        
        else:
          even_tail.next = current
          even_tail = even_tail.next
      
      else:

        if odd_head is None:
          odd_head = current
          odd_tail = odd_head
          
        else:
          odd_tail.next = current
          odd_tail = odd_tail.next
      
      current.next = None
      current = node_next
    
    if odd_head is None:
      return even_head
      
    odd_tail.next = even_head
      

    return odd_head


# helper functions for testing purpose
def create_linked_list(arr):
    if len(arr)==0:
        return None
    head = Node(arr[0])
    tail = head
    for data in arr[1:]:
        tail.next = Node(data)
        tail = tail.next
    return head

def print_linked_list(head):
    while head:
        print(head.data, end=' ')
        head = head.next
    print()

#test function
def test_function(test_case):
    head = test_case[0]
    solution = test_case[1]
    
    node_tracker = dict({})
    node_tracker['nodes'] = list()
    temp = head
    while temp:
        node_tracker['nodes'].append(temp)
        temp = temp.next

    head = even_after_odd(head)    
    temp = head
    index = 0
    try:
        while temp:
            if temp.data != solution[index] or temp not in node_tracker['nodes']:
                print("Fail")
                return
            temp = temp.next
            index += 1
        print("Pass")            
    except Exception as e:
        print("Fail")


arr = [1, 2, 3, 4, 5, 6]
solution = [1, 3, 5, 2, 4, 6]

head = create_linked_list(arr)
test_case = [head, solution]
test_function(test_case)