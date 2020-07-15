"""
Depth first search pre-order with recursion
"""

#create Class Node
class Node(object):
  def __init__(self, value=None):
    self.value = value
    self.left = None
    self.right = None

  def get_value(self):
    return self.value

  def set_value(self, value):
    self.value = value

  def get_left_child(self):
    return self.left
  
  def get_right_child(self):
    return self.right

  def set_left_child(self, node):
    self.left = node
  
  def set_right_child(self, node):
    self.right = node

  def has_left_child(self):
    return self.left != None

  def has_right_child(self):
    return self.right != None

  def __repr__(self):
    s = f"node {self.get_value()}"
    return s


#create class Tree
class Tree(object):
  def __init__(self, value):
    self.root = Node(value)

  def get_root(self):
    return self.root

tree = Tree("Apple")
tree.get_root().set_left_child(Node("Banana"))
tree.get_root().set_right_child(Node("Cherry"))
tree.get_root().get_right_child().set_left_child(Node("Watermeloan"))
tree.get_root().get_left_child().set_left_child(Node("Dates"))
tree.get_root().get_left_child().set_right_child(Node("Leamon"))


def pre_order(tree):
  #basic variables
  visited_order = list()
  root = tree.get_root()
  print(root)
  def traversal(node):
    if node:
      visited_order.append(node.get_value())
      traversal(node.get_left_child())
      traversal(node.get_right_child())
  
  traversal(root)
  return visited_order

print(pre_order(tree))

