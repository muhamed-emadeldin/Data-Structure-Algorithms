#!/usr/bin/env python

#create Node Class
class Node(object):
  def __init__(self, value=None):
    self.value = value
    self.left= None
    self.rigth = None

  def get_value(self):
    return self.value

  def set_value(self, value):
    self.value = value

  def set_left_child(self, node):
    self.left = node
  
  def set_right_child(self, node):
    self.rigth = node

  def get_left_child(self):
    return self.left
  
  def get_right_child(self):
    return self.rigth
  
  def has_left_child(self):
    return self.left != None
  
  def has_right_child(self):
    return self.rigth != None

  def __str__(self):
    return f"Node ({self.get_value()})"


#create Tree Class
class Tree(object):
  def __init__(self, value):
    self.root = Node(value)

  def get_root(self):
    return self.root


#create Stack
class Stack:
  def __init__(self):
    self.arr = list()

  def push(self, value):
    self.arr.append(value)

  def pop(self):
    if self.is_empty():
      return None
    return self.arr.pop()
  
  def top(self):
    if not self.is_empty():
      return self.arr[-1]
    return None

  def is_empty(self):
    return len(self.arr) == 0

  def __repr__(self):
    if not self.is_empty():
      s = "<top of stack>\n_________________\n"
      s += "\n_________________\n".join([str(item) for item in self.arr[::-1]])
      s += "\n_________________\n<bottom of stack>"
      return s

    return "<stack is empty>"


#create State class
class State(object):
  def __init__(self, node):
    self.node = node
    self.visited_left = None
    self.visited_right = None

  def get_value(self):
    return self.node

  def get_visited_left(self):
    return self.visited_left

  def get_visited_right(self):
    return self.visited_right

  def set_visited_left(self):
    self.visited_left = True
  
  def set_visited_right(self):
    self.visited_right = True

  def __repr__(self):
    s= f"""{self.node}
            visited left: {self.visited_left}
            visited right: {self.visited_right}"""
    return s

# create a tree and add some nodes
tree = Tree("apple")
tree.get_root().set_left_child(Node("banana"))
tree.get_root().set_right_child(Node("cherry"))
tree.get_root().get_left_child().set_left_child(Node("dates"))


# # check Stack
# stack = Stack()
# stack.push("apple")
# stack.push("banana")
# stack.push("cherry")
# stack.push("dates")
# print(stack.pop())
# print("\n")
# print(stack)


# visit_order = list()
# stack = Stack()

# # start at the root node, visit it and then add it to the stack
# node = tree.get_root()
# stack.push(node)

# print(f"""
# visit_order {visit_order} 
# stack:
# {stack}
# """)


# visit_order.append(node.get_value())
# print(f"""visit order {visit_order}
# {stack}
# """)

# print(f"{node} has left child {node.has_left_child()}")

# if node.has_left_child:
#   node = node.get_left_child()
#   stack.push(node)

# print(f"""
# visit_order {visit_order} 
# stack:
# {stack}
# """)

# print(f"visit {node}")
# visit_order.append(node.get_value())
# print(f"visit order {visit_order}")

# print(f"{node} has a left child? {node.has_left_child()}")

# if node.has_left_child():
#   node = node.get_left_child()
#   stack.push(node)

# print(f"""visit order {visit_order} 
# stack:
# {stack}""")

# visit_order.append(node.get_value())

# print(f"visit order {visit_order}")

# print(f"{node} has a left child: {node.has_left_child()}")
# print(f"{node} has a right child: {node.has_right_child()}")
# print(stack.pop())
# print(f"stack {stack}")
# print(stack.top())

# print(f"{node} has a right child? {node.has_right_child()}")
# print(f"pop {stack.pop()} off stack")
# print(f"stack {stack}")

# node = stack.top()

# print(f"{node} has a right child? {node.has_right_child()}")

# if node.has_right_child:
#   node = node.get_right_child()
#   stack.push(node)

# print(f"""
# visit_order {visit_order} 
# stack
# {stack}
# """)

# visit_order.append(node.get_value())

# print(f"""visit_order: {visit_order}""")

# # Now we'll check if cherry has a left child
# print(f"{node} has left child? {node.has_left_child()}")

# # it doesn't, so we'll check if it has a right child
# print(f"{node} has right child? {node.has_right_child()}")

# print(f"pop {stack.pop()} off the stack")

# print(f"""
# visit_order {visit_order} 
# stack
# {stack}
# """)

# print(f"pop {stack.pop()} off stack")
# print(f"pre-order traversal visited nodes in this order: {visit_order}")

# def pre_order_with_stack(tree):
#   visit_order = list()
#   stack = Stack()
#   node = tree.get_root()
#   visit_order.append(node.get_value())
#   state = State(node)
#   stack.push(state)

#   while node:
#     if node.has_left_child() and not state.get_visited_left():
#       state.set_visited_left()
#       node = node.get_left_child()
#       visit_order.append(node.get_value())
#       state = State(node)
#       stack.push(state)

#     elif node.has_right_child() and not state.get_visited_right():
#       state.set_visited_right()
#       node = node.get_right_child()
#       visit_order.append(node.get_value())
#       state = State(node)
    
#     else:
#       stack.pop()
#       if not stack.is_empty():
#         state = stack.top()
#         node = state.get_value()
#       else:
#         node = None
    
#   return visit_order

# print(pre_order_with_stack(tree))


def pre_order_recursion(tree):
  #basic variables
  visit_order = list()
  root = tree.get_root()

  def traversal(node):
    if node:
      visit_order.append(node.get_value())
      traversal(node.get_left_child())
      traversal(node.get_right_child())
  traversal(root)
  return visit_order
print(pre_order_recursion(tree))