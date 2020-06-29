#!/usr/bin/env python
"""
Problem Statement
Given a linked list, swap the two nodes present at position i and j, assuming 0 <= i <= j. The positions are based on 0-based indexing.

Note: You have to swap the nodes and not just the values.

Example:

linked_list = 3 4 5 2 6 1 9
positions = 2 5
output = 3 4 1 2 6 5 9
"""

#create class Node
class Node:
  def __init__(self, data=None):
    self.data = data
    self.next = None


"""
:param: head- head of input linked list
:param: `position_one` - indicates position (index) ONE
:param: `position_two` - indicates position (index) TWO
return: head of updated linked list with nodes swapped

TODO: complete this function and swap nodes present at position_one and position_two
Do not create a new linked list
"""

def swap_nodes(head, left_index, right_index):
    
    if head is None :
      return head

    #basic variables
    current = head

    #garb previous, current, next
    node = None
    previous = None
    next_node = None

    #store values of one posation and tw posation
    swap_right = None
    swap_left = None
    index = 1

    while current:
      #grab previous node
      index += 1
      if previous is None:
        previous  = current
      else:
        previous  = current.next
      
      node        =  current.next.next
      next_node   = node.next

      if index == left_index:
        swap_right = node
        previous.next = next_node
        swap_left = previous.next

      if index == right_index:
        swap_left.next = swap_right
        swap_right.next = node
        
        
      current = current.next
      

    return head


# Test - Let's test your function
def test_function(test_case):
    head = test_case[0]
    left_index = test_case[1]
    right_index = test_case[2]
    
    left_node = None
    right_node = None
    
    temp = head
    index = 0
    try:
        
        while temp is not None:
            if index == left_index:
                left_node = temp
            if index == right_index:
                right_node = temp
                break
            index += 1
            temp = temp.next

        updated_head = swap_nodes(head, left_index, right_index)
        
        temp = updated_head
        index = 0
        pass_status = [False, False]

        while temp is not None:

            if index == left_index:
                pass_status[0] = temp is right_node
            
            if index == right_index:
                pass_status[1] = temp is left_node

            index += 1
            temp = temp.next
            

        if pass_status[0] and pass_status[1]:
            print("Pass")
        else:
            print("Fail")
        return updated_head
    except Exception as e:
        print("Fail")



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
        print(head.data, end=" ")
        head = head.next
    print()


arr = [3, 4, 5, 2, 6, 1, 9]
head = create_linked_list(arr)
left_index = 3
right_index = 4
test_case = [head, left_index, right_index]

updated_head = test_function(test_case)
print_linked_list(test_case[0])