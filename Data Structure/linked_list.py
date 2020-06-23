'''
Linked List Practice
Implement a linked list class. You have to define a few functions that perform the desirbale action. Your LinkedList class should be able to:

Append data to the tail of the list and prepend to the head
Search the linked list for a value and return the node
Remove a node
Pop, which means to return the first node's value and delete the node from the list
Insert data at some position in the list
Return the size (length) of the linked list
'''


#created Node class
class Node:
  def __init__(self, value):
    self.value = value
    self.next = None
    self.previous = None

#create linked list
class LinkedList:
  def __init__(self):
    self.head = None

  
  def to_list(self):
    out_list = []
    node = self.head
    
    while node:
      out_list.append(node.value)
      node = node.next

    return out_list

# Define a function outside of the class
def prepend(self, value):
    """ Prepend a value to the beginning of the list."""
    # TODO: Write function to prepend here
    if self.head is None:
      self.head = Node(value)
      return

    node = Node(value)
    node.next = self.head
    self.head = node


def append(self, value):

  if self.head is None:
    self.head = Node(value)
    return

  node = self.head
  while node.next:
    node = node.next
  node.next = Node(value)
  return 

def search(self, value):
    """ Search the linked list for a node with the requested value and return the node. """
    # TODO: Write function to search here
    if self.head is None:
      return None

    node = self.head
    new_node = Node(value)
    
    while node:
      if node.value == new_node.value:
        return node       
      node = node.next


def remove(self, value):
    """ Remove first occurrence of value. """
    # TODO: Write function to remove here
    if self.head is None:
      return None
    
    new_node = Node(value)

    if self.head.value == value:
        self.head = self.head.next
        return

    node = self.head
    while node:
      if node.next != None:
        if node.next.value == value:
          node.next = node.next.next
          return
      node = node.next

    
def pop(self):
    """ Return the first node's value and remove it from the list. """
    # TODO: Write function to pop here
    if self.head is None:
      return None

    node= self.head
    self.head = self.head.next
    
    
    return node.value

def insert(self, value, pos):
    """ Insert value at pos position in the list. If pos is larger than the
    length of the list, append to the end of the list. """
    
    if self.head is None:
      self.head = Node(value)
      return

    node = self.head
    
    
    cont = 0
    if pos == cont:
      self.head = Node(value)
      self.head.next = node
    
    node = self.head

    while node:
      cont += 1
      if pos == cont:
        node_next = node.next
        node.next = Node(value)
        node.next.next = node_next
      
      node = node.next
    
    if pos > cont:
      node = Node(value)
      self.append(node.value)



def size(self):
    """ Return the size or length of the linked list. """
    # TODO: Write function to get size here
    if self.head is None:
      return
    
    node = self.head
    cont = 0
    while node:
      cont += 1
      node = node.next

    return cont

      
# Test prepend
LinkedList.prepend = prepend
linked_list = LinkedList()
linked_list.prepend(1)
assert linked_list.to_list() == [1], f"list contents: {linked_list.to_list()}"

# Test append - 1
LinkedList.append = append
linked_list.append(3)
linked_list.prepend(2)
assert linked_list.to_list() == [2, 1, 3], f"list contents: {linked_list.to_list()}"

# Test append - 2
linked_list = LinkedList()
linked_list.append(1)
assert linked_list.to_list() == [1], f"list contents: {linked_list.to_list()}"
linked_list.append(3)
assert linked_list.to_list() == [1, 3], f"list contents: {linked_list.to_list()}"

# Test search
LinkedList.search = search
linked_list.prepend(2)
linked_list.prepend(1)
linked_list.append(4)
linked_list.append(3)
assert linked_list.search(1).value == 1, f"list contents: {linked_list.to_list()}"
assert linked_list.search(4).value == 4, f"list contents: {linked_list.to_list()}"

# Test remove
LinkedList.remove = remove
linked_list.remove(1)
assert linked_list.to_list() == [2, 1, 3, 4, 3], f"list contents: {linked_list.to_list()}"
linked_list.remove(3)
assert linked_list.to_list() == [2, 1, 4, 3], f"list contents: {linked_list.to_list()}"
linked_list.remove(3)
assert linked_list.to_list() == [2, 1, 4], f"list contents: {linked_list.to_list()}"

# Test pop
LinkedList.pop = pop
value = linked_list.pop()
assert value == 2, f"list contents: {linked_list.to_list()}"
assert linked_list.head.value == 1, f"list contents: {linked_list.to_list()}"


# Test insert 
LinkedList.insert = insert
linked_list.insert(5, 0)
assert linked_list.to_list() == [5, 1, 4], f"list contents: {linked_list.to_list()}"
linked_list.insert(2, 1)
assert linked_list.to_list() == [5, 2, 1, 4], f"list contents: {linked_list.to_list()}"
linked_list.insert(3, 6)
assert linked_list.to_list() == [5, 2, 1, 4, 3], f"list contents: {linked_list.to_list()}"

# Test size function
LinkedList.size = size
assert linked_list.size() == 5, f"list contents: {linked_list.to_list()}"