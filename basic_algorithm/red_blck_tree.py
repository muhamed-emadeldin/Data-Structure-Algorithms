#!/usr/bin/env python

'''
Implement Red Black Tree:
Rules:
1- All nodes have a color
2- the root node color must be black
3- All null nodes have color black
4- All nodes have children
5- the tree does not contain two red nodes
6- Every path to its descendent null nodes must contain the same number of black nodes

The trick of the tree:
if aunt node color red we must use color flip way:
parent color red and children color black

if aunt node color black we must use rotation way:
1- grandparent and parent and node in the same way
2- child left side of parent and parent right side of grandparent
'''

#--> create Class Node
class Node:
  def __init__(self, value=None, parent=None, color=""):
    self.value  = value
    self.parent = parent
    self.color  = color
    self.left   = None
    self.right  = None

  def __repr__(self):
    print_color = 'R' if self.color == 'red' else 'B'
    return '%d%s' % (self.value, print_color)

#--> create RedBlackTree
class RedBlackTree:
  #--> Initial function
  def __init__(self, root):
    self.root = Node(root, None, "red")
    self.size = 0

  #--> insert new node
  def insert(self, value):
    node = self.insert_helper(self.root, value)
    self.rebalance(node)
    self.size += 1

  #--> insert helper function
  def insert_helper(self, curr, new_val):
    if curr.value > new_val:
      if curr.left:
        insert_helper(curr.left, new_val)
      else:
        curr.left = Node(new_val, curr, "red")
        return curr.left
    
    else:
      if curr.right:
        insert_helper(curr.right, new_val)
      else:
        curr.right = Node(new_val, curr, "red")
        return curr.right

  #--> get grand parent node
  def get_grand_parent(self, node):
    p = node.parent
    if p is None:
      return None
    return node.parent.parent

  #--> get aunt node
  def get_aunt_node(self, node):
    p = node.parent
    gp = self.get_grand_parent(node)

    if gp is None:
      return None
    
    if p == gb.left:
      return gp.right
    
    if p == gp.right:
      return gp.left

  #--> rebalance tree
  def rebalance(self, node):
    #--> Case 1: if node == root
    if node.parent is None:
      return
    
    #--> Case 2: if parent color black
    if node.parent.color == "black":
      return

    #--> Case 3: if we have two nodes have color red and aunt of new node is red
    if self.get_aunt_node(node) and self.get_aunt_node(node).color == "red":
      self.get_grand_parent(node).color = "red"
      self.get_aunt_node(node).color    = "black"
      node.parent.color                 = "black"
      return self.rebalance(self.get_grand_parent(node))

    gp = self.get_grand_parent(node)

    #-->defense function
    if gp is None:
      return None
    
    #--> Case 4 & Case 5: if we have two node have color is red and aunt of new node is black
    #--> if path from grand parent to new node is left to right
    if gp.left and node == gb.left.right:
      self.rotation_left(p)
      node = node.left
    #--> if path from grand parent to new node is right to left
    elif gp.right and node == gb.right.left:
      self.rotation_right(p)
      node = node.right
    
    p = node.parent
    gp = p.parent
    #--> if path from grand parent to new node is left to left
    if node == p.left:
      self.rotation_right(gp)
    else:
    #--> if path from grand parent to new node is right to right
      self.rotation_left(gb)
    
    p.color = "black"
    gp.color = "red"


  #--> right rotation
  def rotation_left(self, node):
    p = node.parent
    node_moving_up = node.right
    node.right = node_moving_up.left
    # 'node' moves down, to being a left child
    node_moving_up.left = node
    node.parent = node_moving_up

    # Now we need to connect to the sub-tree's parent
    # 'node' may have been the root
    if p != None:
        if node == p.left:
            p.left = node_moving_up
        else:
            p.right = node_moving_up
    node_moving_up.parent = p

  def rotate_right(self, node):
      p = node.parent

      node_moving_up = node.left
      node.left = node_moving_up.right

      node_moving_up.right = node
      node.parent = node_moving_up

      # Now we need to connect to the sub-tree's parent
      if p != None:
          if node == p.left:
              p.left = node_moving_up
          else:
              p.right = node_moving_up
      node_moving_up.parent = p

def print_tree(node, level=0):
    print('   ' * (level - 1) + '+--' * (level > 0) + '%s' % node)
    if node.left:
        print_tree(node.left, level + 1)
    if node.right:
        print_tree(node.right, level + 1)

tree = RedBlackTree(9)
tree.insert(6)
tree.insert(19)

print_tree(tree.root)