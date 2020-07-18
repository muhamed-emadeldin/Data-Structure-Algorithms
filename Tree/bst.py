#!/usr/bin/env python

"""
Binary Search Tree
"""

# this code makes the tree that we'll traverse

class Node(object):
        
    def __init__(self,value = None):
        self.value = value
        self.left = None
        self.right = None
        
    def set_value(self,value):
        self.value = value
        
    def get_value(self):
        return self.value
        
    def set_left_child(self,left):
        self.left = left
        
    def set_right_child(self, right):
        self.right = right
        
    def get_left_child(self):
        return self.left
    
    def get_right_child(self):
        return self.right

    def has_left_child(self):
        return self.left != None
    
    def has_right_child(self):
        return self.right != None
    
    # define __repr_ to decide what a print statement displays for a Node object
    def __repr__(self):
        return f"Node({self.get_value()})"
    
    def __str__(self):
        return f"Node({self.get_value()})"


from collections import deque
class Queue():
    def __init__(self):
        self.q = deque()
        
    def enq(self,value):
        self.q.appendleft(value)
        
    def deq(self):
        if len(self.q) > 0:
            return self.q.pop()
        else:
            return None
    
    def __len__(self):
        return len(self.q)
    
    def __repr__(self):
        if len(self.q) > 0:
            s = "<enqueue here>\n_________________\n" 
            s += "\n_________________\n".join([str(item) for item in self.q])
            s += "\n_________________\n<dequeue here>"
            return s
        else:
            return "<queue is empty>"


class Tree():
    def __init__(self):
        self.root = None
        
    def set_root(self,value):
        self.root = Node(value)
        
    def get_root(self):
        return self.root
    
    def compare(self,node, new_node):
        """
        0 means new_node equals node
        -1 means new node less than existing node
        1 means new node greater than existing node 
        """
        if new_node.get_value() == node.get_value():
            return 0
        elif new_node.get_value() < node.get_value():
            return -1
        else:
            return 1
    
    """
    define insert here
    can use a for loop (try one or both ways)
    """
    def insert(self,new_value):
        new_node = Node(new_value)
        node = self.get_root()
        if node == None:
            self.root = new_node
            return
        
        while(True):
            comparison = self.compare(node, new_node)
            if comparison == 0:
                # override with new node
                node = new_node
                break # override node, and stop looping
            elif comparison == -1:
                # go left
                if node.has_left_child():
                    node = node.get_left_child()
                else:
                    node.set_left_child(new_node)
                    break #inserted node, so stop looping
            else: #comparison == 1
                # go right
                if node.has_right_child():
                    node = node.get_right_child()
                else:
                    node.set_right_child(new_node)
                    break # inserted node, so stop looping
                
                

    """
    define insert here (can use recursion)
    try one or both ways
    """  
    def insert_with_recursion(self,value):
        #basic variables
        new_node = Node(value)
        node = self.get_root()
        if self.root is None:
          self.root = new_node
        else:
          self.recursive_insert(node, new_node)
    
    def recursive_insert(self, node, new_node):
      compare = self.compare(node, new_node)
      if compare == 0:
        node = node.set_value(new_node)
      elif compare == -1:
        if node.has_left_child():
          node = node.get_left_child()
          self.recursive_insert(node, new_node)
        else:
          node = node.set_left_child(new_node)

      elif compare == 1:
        if node.has_right_child():
          node = node.get_right_child()
          self.recursive_insert(node, new_node)
        else:
          node.set_right_child(new_node)
    

    """
    implement search
    """
    def search(self,value):
        #basic variables
        search_node = Node(value)
        root = self.get_root()
        while True:
          compare = self.compare(root, search_node)
          if compare == 0:
            return True
            break
          elif compare == -1:
            if root.has_left_child():
              root = root.get_left_child()
            else:
              return False
              break
          elif compare == 1:
            if root.has_right_child():
              root = root.get_right_child()
            else:
              return False
              break

    def minValue(self,node):
      current = node
      while current.get_left_child() is not None:
        current = current.get_left_child()
      
      return current

    def delete(self, value):
      node = self.get_root()
      key = Node(value)
      parent = None

      #defense function
      if not self.search(value) or node is None:
        return None
      
      #traversal delete
      def traversal(node, key, parent):
        compare = self.compare(node, key)

        #we start operations when we found key
        if compare == 0:
          print("found", parent)
          # Set case3: node has two leafs
          if node.has_right_child() and node.has_left_child():
            node_right = node.get_right_child()
            node_left = node_right.get_left_child()
            if not node_left is None:
              value = self.minValue(node_left)
            else:
              value = self.minValue(node_right)
            traversal(node, value, parent)
            node = node.set_value(value.get_value())
            print("node is:", node, "parent is", parent, "key is", value)

          '''
            Seat case1: node hasn't leafs and Set case2: node has one leaf
          '''
          elif parent.get_left_child() == node:
            parent.set_left_child(node.get_left_child())
          
          elif parent.get_right_child() == node:
            parent.set_right_child(node.get_right_child())

          
            

          key = None
          print("key equal after operation", key)
        
        if compare == -1:
          print("node in the left")
          parent = node
          node = node.get_left_child()
          traversal(node, key, parent)
        
        if compare == 1:
          print("node in the right")
          parent = node
          node = node.get_right_child()
          traversal(node, key, parent)

      traversal(node, key, parent)

    def __repr__(self):
        level = 0
        q = Queue()
        visit_order = list()
        node = self.get_root()
        q.enq( (node,level) )
        while(len(q) > 0):
            node, level = q.deq()
            if node == None:
                visit_order.append( ("<empty>", level))
                continue
            visit_order.append( (node, level) )
            if node.has_left_child():
                q.enq( (node.get_left_child(), level +1 ))
            else:
                q.enq( (None, level +1) )

            if node.has_right_child():
                q.enq( (node.get_right_child(), level +1 ))
            else:
                q.enq( (None, level +1) )

        s = "Tree\n"
        previous_level = -1
        for i in range(len(visit_order)):
            node, level = visit_order[i]
            if level == previous_level:
                s += " | " + str(node) 
            else:
                s += "\n" + str(node)
                previous_level = level

                
        return s


# tree = Tree()
# tree.insert_with_loop(5)
# tree.insert_with_loop(6)
# tree.insert_with_loop(4)
# tree.insert_with_loop(2)
# tree.insert_with_loop(5) # insert duplicate
# print(tree)

# tree = Tree()
# tree.insert_with_recursion(5)
# tree.insert_with_recursion(6)
# tree.insert_with_recursion(4)
# tree.insert_with_recursion(2)
# tree.insert_with_recursion(5) # insert duplicate
# print(tree)


tree = Tree()
# tree.insert(50)
# tree.insert(30)
# tree.insert(20)
# tree.insert(40)
# tree.insert(70)
# tree.insert(60)
# tree.insert(80)
tree.insert(25)
tree.insert(9)
tree.insert(30)
tree.insert(8)
tree.insert(12)
tree.insert(29)
tree.insert(38)
tree.insert(7)
tree.insert(8.5)
tree.insert(11)
tree.insert(13)
tree.insert(28)
tree.insert(36)
tree.insert(40)






# tree.insert(5)
# tree.insert(3)
# tree.insert(2)
# tree.insert(4)
# tree.insert(7)
# tree.insert(6)
# tree.insert(10)
# tree.insert(9)
# tree.insert(8)
# tree.insert(8.5)

# tree.insert(10)
# tree.insert(11)
# tree.insert(3)
# tree.insert(2)
# tree.insert(1)

# print(f"""
# search for 8: {tree.search(8)}
# search for 2: {tree.search(2)}
# search for 4: {tree.search(4)}
# search for 5: {tree.search(5)}
# search for 6: {tree.search(6)}
# search for 1: {tree.search(1)}
# """)
tree.delete(12)
# print(f"""
# delete for 4: {tree.delete(4)}
# """)
print(tree)