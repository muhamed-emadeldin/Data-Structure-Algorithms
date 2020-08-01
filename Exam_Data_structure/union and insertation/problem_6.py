#!/usr/bin/env python

#create Node class
class Node:
  def __init__(self, data):
    self.data = data
    self.next = None


#created LinkedList
class LinkedList:

  #initial defenation
  def __init__(self):
    self.head = None

  #append defenation
  def append(self, data):
    new_node = Node(data)

    if self.head is None:
      self.head = new_node
      return
    node = self.head

    while node.next:
      node  = node.next
    
    node.next = new_node

  #remove and retun node function
  def pop(self):
    if self.head is None:
      return None

    node = self.head
    self.head = self.head.next
    return node

  #Search function to get the repeated items
  def search(self, data):
    node = self.head
    if node is None:
      return None

    while node:
      if node.data == data:
        return True
      node = node.next
    return False

  #append all nodes in list
  def to_list(self):
    out_list = []
    node = self.head

    while node:
      out_list.append(node.data)
      node = node.next
    
    return out_list

  #num of nodes
  def size(self):
    return len(self.to_list())


  def __str__(self):
    cur_head = self.head
    out_string = ""
    while cur_head:
        out_string += str(cur_head.data) + " -> "
        cur_head = cur_head.next
    if len(out_string) > 0:
      return out_string
    else:
      return "Linked List is empty!!"


def union(llist_1, llist_2):
  #defense function
  if not isinstance(llist_1, LinkedList) and not isinstance(llist_2, LinkedList):
    return "Type of inputs should be Linked list"
  elif llist_1 is None or llist_2 is None or llist_1 == "" or llist_2 == "":
    return None

  #basic variables
  union_linked_list = LinkedList()
  list1 = llist_1.to_list()
  list2 = llist_2.to_list()

  def dry_code(ls1, ls2):
    if union_linked_list.head is None:
      union_linked_list.append(ls1[0])
      if union_linked_list.search(ls2[0]) is False:
        union_linked_list.append(ls2[0])
    
    for i in range(1, len(ls1)):
      if union_linked_list.search(ls1[i]) is False:
        union_linked_list.append(ls1[i])

      if i < len(ls2):
        if union_linked_list.search(ls2[i]) is False:
          union_linked_list.append(ls2[i])

  if len(list1) > len(list2):
    dry_code(list1, list2)
  else:
    dry_code(list2, llist_1)

  return union_linked_list

def intersection(llist_1, llist_2):
  # Your Solution Here
  #defense function
  if not isinstance(llist_1, LinkedList) and not isinstance(llist_2, LinkedList):
    return "Type of inputs should be Linked list"
  if llist_1 is None or llist_2 is None or llist_1 == "" or llist_2 == "":
    return None
  

  #basic variables
  inter_linked_list = LinkedList()
  list1 = llist_1.to_list()
  list2 = llist_2.to_list()

  def dry_code(ls1, ls2):
    for node in ls1:
      if ls2.search(node) is True:
        if inter_linked_list.head is None:
          inter_linked_list.append(node)
        else:
          if inter_linked_list.search(node) is False:
            inter_linked_list.append(node)

  if len(list1) > len(list2):
    dry_code(list1, llist_2)
  else:
    dry_code(list2, llist_1)

  return inter_linked_list
    


# Test case 1

linked_list_1 = LinkedList()
linked_list_2 = LinkedList()

element_1 = [3,2,4,35,6,65,6,4,3,21]
element_2 = [6,32,4,9,6,1,11,21,1]

for i in element_1:
    linked_list_1.append(i)

for i in element_2:
    linked_list_2.append(i)

# function Test
def union_test_cases():
  test_cases = [((None, None), "Type of inputs should be Linked list"),
                ((None, linked_list_2), None),
                ((linked_list_1, ""), None),
                ((linked_list_1, linked_list_2), [3,6,2,32,4,35,9,65,1,11,21]),
               ]
  
  for (args, answer) in test_cases:
    try:
      result = union(*args)
      if result == answer and answer != "AssertionError" or result.to_list() == answer:
        print("Test case year passed!")
      else:
        print("Test with data:", args, "failed")
    
    except AssertionError:
          if answer == "AssertionError":
              print( "Nice job! Test case {0} correctly raises AssertionError!\n".format(args))
          else:
              print("Check your work! Test case {0} should not raise AssertionError!\n".format(args))

  
union_test_cases()


def insert_test_cases():
  test_cases = [((None, None), "Type of inputs should be Linked list"),
                ((None, linked_list_2), None),
                ((linked_list_1, ""), None),
                ((linked_list_1, linked_list_2), [4, 6, 21]),
               ]
  
  for (args, answer) in test_cases:
    try:
      result = intersection(*args)
      if result == answer and answer != "AssertionError" or result.to_list() == answer:
        print("Test case year passed!")
      else:
        print("Test with data:", args, "failed")
    
    except AssertionError:
          if answer == "AssertionError":
              print( "Nice job! Test case {0} correctly raises AssertionError!\n".format(args))
          else:
              print("Check your work! Test case {0} should not raise AssertionError!\n".format(args))

  
insert_test_cases()



# # Test case 2

linked_list_3 = LinkedList()
linked_list_4 = LinkedList()

element_1 = [3,2,4,35,6,65,6,4,3,23]
element_2 = [1,7,8,9,11,21,1]

for i in element_1:
    linked_list_3.append(i)

for i in element_2:
    linked_list_4.append(i)



# function Test
def union_test_cases_2():
  test_cases = [((None, None), "Type of inputs should be Linked list"),
                ((None, linked_list_4), None),
                ((linked_list_3, ""), None),
                ((linked_list_3, linked_list_4), [3,1,2,7,4,8,35,9,6,11,65,21,23]),
               ]
  
  for (args, answer) in test_cases:
    try:
      result = union(*args)
      if result == answer and answer != "AssertionError" or result.to_list() == answer:
        print("Test case union passed!")
      else:
        print("Test with data:", args, "failed")
    
    except AssertionError:
          if answer == "AssertionError":
              print( "Nice job! Test case {0} correctly raises AssertionError!\n".format(args))
          else:
              print("Check your work! Test case {0} should not raise AssertionError!\n".format(args))

  
union_test_cases_2()


def insert_test_cases_2():
  test_cases = [((None, None), "Type of inputs should be Linked list"),
                ((None, linked_list_4), None),
                ((linked_list_3, ""), None),
                ((linked_list_3, linked_list_4), []),
               ]
  
  for (args, answer) in test_cases:
    try:
      result = intersection(*args)
      if result == answer and answer != "AssertionError" or result.to_list() == answer:
        print("Test case insertation passed!")
      else:
        print("Test with data:", args, "failed")
    
    except AssertionError:
          if answer == "AssertionError":
              print( "Nice job! Test case {0} correctly raises AssertionError!\n".format(args))
          else:
              print("Check your work! Test case {0} should not raise AssertionError!\n".format(args))

  
insert_test_cases_2()

