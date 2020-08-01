#!/usr/bin/env python


import sys, heapq

#create class Node
class Node:
  def __init__(self, chr=None, freq=None):
    self.chr    = chr
    self.freq   = freq
    self.left   = None
    self.right  = None
  
  def get_left_child(self):
    return self.left
  
  def get_right_child(self):
    return self.right
  
  def set_left_child(self, node):
    self.left = node
  
  def set_rigth_child(self, node):
    self.right = node
  
  def has_left_child(self):
    return self.left != None
  
  def has_right_child(self):
    return self.right != None
  
  def __lt__(self, other):
    return self.freq < other.freq
  
  def __eq__(self, other):
    if other is None or not isinstance(other, Node):
      return False
    
    return self.freq == other.freq


#create class Queue
class Queue:

  def __init__(self):
    self.storage = []
  
  def enq(self, node):
    self.storage.append(node)
  
  def deq(self):
    return self.storage.pop(0)
  
  def __len__(self):
    return len(self.storage)
  

#create Huffman Tree
class HuffmanTree:
  def __init__(self):
    self.root = None
    self.heap = []
    self.codes = {}
  
  def get_root(self):
    return self.root

  #build frequency dictionary
  def make_frequency_dictionary(self, string):
    frequency = {}
    for chr in string:
      if not chr in frequency:
        frequency[chr] = 0
      frequency[chr] += 1
    return frequency

  #store in priority queue
  def make_heap(self, frequncy):
    for chr, freq in frequncy.items():
      node = Node(chr, freq)
      heapq.heappush(self.heap, node)
  
  #building root in huffman tree
  def merge_codes(self):
    if len(self.heap) == 1:
      node = self.heap[0]
      self.root = Node(node.chr, node.freq)
      self.root.set_left_child(None)
      self.root.set_rigth_child(None)

    while len(self.heap) > 1:
      node1 = heapq.heappop(self.heap)
      node2 = heapq.heappop(self.heap)
      freq_two_nodes = node1.freq + node2.freq
      merge_node = Node(None, freq_two_nodes)
      self.root = merge_node
      self.root.set_left_child(node1)
      self.root.set_rigth_child(node2)
      heapq.heappush(self.heap, merge_node)
    

  #make helper code
  def make_code_helper(self, node, code):
    #defense function
    if node is None:
      return False

    if node.chr != None:
      self.codes[node.chr] = code

    self.make_code_helper(node.get_left_child(), code + "0")
    self.make_code_helper(node.get_right_child(), code + "1")
    

  #make codes for each charater
  def make_code(self, string):
    root = heapq.heappop(self.heap)
    self.make_code_helper(root, "")
  
  #make encode for string
  def get_encode_string(self, string):
    encode_str = ""
    for chr in string:
      encode_str += self.codes[chr]
    return encode_str

  
  #print tree
  def __str__(self):
    level = 0
    q = Queue()
    visit_order = list()
    node = self.get_root()
    q.enq(( (node,level) ))
    while(len(q) > 0):
        node, level = q.deq()
        if node == None:
            visit_order.append( ("<empty>", level))
            continue
        visit_order.append( (node.freq, level) )
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


def huffman_encoding(data):
  #defense function
  if not isinstance(data, str) or data == "":
    return -1
    
  tree = HuffmanTree()
  #calculate count of charater in string
  frequncy = tree.make_frequency_dictionary(data)
  tree.make_heap(frequncy)
  tree.merge_codes()
  tree.make_code(data)
  encoded_data = tree.get_encode_string(data)
  

  #--> Edge case if huffman tree contains only a root
  if encoded_data == "":
    _range = tree.get_root().freq
    for i in range(_range):
      encoded_data += str(0)

  return encoded_data, tree


def huffman_decoding(data,tree):
  #defense function
  if not isinstance(tree, HuffmanTree):
    return -1
  if data is None or not data.isdigit():
    return -1

  string = ""
  cont = 0
  node = tree.get_root()

  #edge case
  if not node.has_left_child() and not node.has_right_child():
    for i in range(len(data)):
      chr = tree.get_root().chr
      string += chr
  else:
    while cont < len(data):
      #condition if left child and right child of node is none return to root
      if not node.has_left_child() and not node.has_right_child():
        node = tree.get_root()

      #check if character in posation left
      if data[cont] == "1":
        node = node.get_right_child()
        if node is not None and node.chr != None:
          string += node.chr

      #check if character in posation right
      elif data[cont] == "0":
        node = node.get_left_child()
        if node is not None and node.chr != None:
          string += node.chr
      
      cont += 1

  return string


#Edge case if data is empty string
assert huffman_encoding("") == -1
#Edge case if data is None
assert huffman_encoding(None) == -1


# function Test
def test_cases_encode():
  test_cases = [
                (("AAAAAAABBBCCCCCCCDDEEEEEE",), ("1010101010101000100100111111111111111000000010101010101",)),

                (("The bird is the word",), ("1000111111100100001101110000101110110110100011111111001101010011100001",)),

                (("hello world",), ("01011111010110000011110111010001",)),

                (("My code is correct",), ("011001001101110010111000110100010011101110011011010001110101",)),

                (("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUV",), ("11000010111011000111111110111110001101000110111101010101000001100001000100111000010011101011101001101101010111111101010011000010011111110100011000010010110010111100101101110010100000101101101100011110111011110010011110011000000100010111011111010100100010110101001100110011",)),


                (("m",), ("0",)),


                (("mmmmm",), ("00000",)),
                
               ]
  
  for (args, answer) in test_cases:
    try:
      result, tree = huffman_encoding(*args)
      if result == answer[0] and answer != "AssertionError":
        print("Test case encode passed!")
      else:
        print("Test with data encode:", args, "failed")
    
    except AssertionError:
          if answer == "AssertionError":
              print( "Nice job! Test case {0} correctly raises AssertionError!\n".format(args))
          else:
              print("Check your work! Test case {0} should not raise AssertionError!\n".format(args))

  
test_cases_encode()




#Edge case if data is empty string
assert huffman_decoding("", HuffmanTree()) == -1
#Edge case if data is None
assert huffman_decoding(None, HuffmanTree()) == -1
#Edge case if data is empty string
assert huffman_decoding("", None) == -1



def test_cases_decode():
  test_cases = [("AAAAAAABBBCCCCCCCDDEEEEEE", "AAAAAAABBBCCCCCCCDDEEEEEE"),
                ("The bird is the word", "The bird is the word"),
                ("hello world", "hello world"),
                ("My code is correct", "My code is correct"),
                ("m", "m"),
                ("mm", "mm"),
               ]
  
  for args, answer in test_cases:
    try:
      encoded_data, tree = huffman_encoding(args)
      result  = huffman_decoding(encoded_data, tree)
      if result == answer and answer != "AssertionError":
        print("Test case decode passed!")
      else:
        print("Test with data decode:", args, "failed")
    
    except AssertionError:
          if answer == "AssertionError":
              print( "Nice job! Test case {0} correctly raises AssertionError!\n".format(args))
          else:
              print("Check your work! Test case {0} should not raise AssertionError!\n".format(args))

  
test_cases_decode()



# if __name__ == "__main__":
#     codes = {}

#     a_great_sentence = "mm"

#     print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
#     print ("The content of the data is: {}\n".format(a_great_sentence))

#     encoded_data, tree = huffman_encoding(a_great_sentence)
#     print(encoded_data)
#     # print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
#     # print ("The content of the encoded data is: {}\n".format(encoded_data))

#     decoded_data = huffman_decoding(encoded_data, tree)

#     print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
#     print ("The content of the encoded data is: {}\n".format(decoded_data))