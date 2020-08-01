#!/usr/bin/env python

import hashlib
import datetime

class Block:
  def __init__(self, timestamp=None, data=None, previous_hash=None):
    self.timestamp = timestamp
    self.data = data
    self.previous_hash = previous_hash
    self.hash = self.calc_hash()
    self.next = None

  def calc_hash(self):
    sha = hashlib.sha256()
    hash_str = self.data.encode("utf-8")
    sha.update(hash_str)
    return sha.hexdigest()

  def __repr__(self):
    s = ""
    s += "Universal Time:" + str(self.timestamp) + " ,"
    s += "Data is:" + str(self.data) + " ,"
    s += "Previous Hash is:" + str(self.previous_hash) + " ,"
    s += "Hash:" + str(self.hash)
    return s

#create LinkedListNode 
class BlockChainLinkedList:
  def __init__(self):
    self.head = None
    self.tail = None

  def append(self, value):
    #defense function
    if value is None or value == "":
      return None
    

    elif self.head is None:
      self.head = Block(datetime.datetime.utcnow(), value, 0)
      self.tail = self.head
    
    else:
      self.tail.next = Block(datetime.datetime.utcnow(), value, self.tail.hash)
      self.tail = self.tail.next

    return

  def search(self, data):
    if self.head is None:
      return None

    block = self.head

    while block is not None:
      if block.data == data:
        return True
      block = block.next
    return False

  def pop(self):
    #defense function
    if self.head is None:
      return None

    block = self.head
    self.head = self.head.next

    return block

  def to_list(self):
    out_list = []
    block = self.head
    if not block is None:
      while block:
        out_list.append([block])
        block = block.next
    if len(out_list) > 0:
      return out_list
    return None

  def size(self):
    return len(self.to_list())




#Edge case if capacity < 1
block1 = BlockChainLinkedList()
assert block1.append("") == None

#Edge case if capacity is None
block2 = BlockChainLinkedList()
assert block2.append(None) == None



block = BlockChainLinkedList()
data1 = "Representing Transactions"
data2 = "Creating Blocks"
data3 = "Generating Block Hashes"
data4 = "Hashing and SHA-256"
block.append(data1)
block.append(data2)
block.append(data3)
block.append(data4)


# function test_cases_append
def test_cases_search():
  test_cases = [#Edge case if value is empty string
                ("", False),
                #Edge case if value is None
                (None, False),
                #Edge case if a value is not exists
                ("data10", False),
                
                (data1, True),
                (data2, True),
                (data3, True),
               ]
  
  for args, answer in test_cases:
    try:
      result = block.search(args)
      if result == answer and answer != "AssertionError":
        print("Test case blockshain passed!")
      else:
        print("Test with data:", args, "failed")
      

    
    except AssertionError:
          if answer == "AssertionError":
              print( "Nice job! Test case {0} correctly raises AssertionError!\n".format(args))
          else:
              print("Check your work! Test case {0} should not raise AssertionError!\n".format(args))

  
test_cases_search()
