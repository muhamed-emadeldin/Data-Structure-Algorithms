#!/usr/bin/env python

# #--> Building a Trie in Python
class TrieNode:
  #-->initial function
  def __init__(self):
    self.is_word = False
    self.children = {}

  def insert(self, chr):
    self.children[chr] = TrieNode()



class Trie:
  #--> initial function
  def __init__(self):
    self.root = TrieNode()

  #--> insert function
  def insert(self, word):
    curr_node = self.root
    
    for chr in word:
      if not chr in curr_node.children:
        curr_node.insert(chr)
      curr_node = curr_node.children[chr]
    
    curr_node.is_word = True

  #-->find function
  def find(self, word):
    #-->defense function
    assert(isinstance(word, str)), "AssertionError"
    if word == "":
      return None

    #--basic variable
    curr_node = self.root

    for chr in word:
      if not chr in curr_node.children:
        return "we can't complete this suffix"
      curr_node = curr_node.children[chr]

    return curr_node

  
#################################################Step2#############################################

#--> Finding Suffixes
class TrieNode:
  #--> initial function
  def __init__(self):
    self.children = {}
    self.is_word  = False
    self.word_list   = []
    

  #-->insert function
  def insert(self, chr):
    self.children[chr] = TrieNode()

  #-->suffic function
  def suffixes(self, suffix = ''):
    #-->basic variable
    children = self.children

    #-->defense function
    assert(isinstance(suffix, str)), "AssertionError"

    if suffix == "":
      return "AssertionError"

    if children:
      for chr , node in children.items():
        self.autocomplete(node, chr)
    return self.word_list
  

  #-->autocomplete function
  def autocomplete(self, node, word):
    if node.is_word:
      self.word_list.append(word)
    
    for k,v in node.children.items():
      self.autocomplete(v, word + k)



MyTrie = Trie()
wordList = [
    "fun", "function", "factory", 
    "ant", "anthology", "antagonist", "antonym", 
    "trie", "trigger", "trigonometry", "tripod",
    "cat", "class", "cow", "closer", "clear",
    "udacity", "under", "up", "uber", "unique"
]
for word in wordList:
    MyTrie.insert(word)

def router_test():
  test_cases  = [#-->Edge cases
                  (None, "AssertionError"),#-->'AssertionError'
                  ("", "AssertionError"),#-->None

                  ("f", ["un", "unction", "actory"]),
                  ("a", ["nt", "nthology", "ntagonist", "ntonym"]),
                  ("t", ["rie", "rigger", "rigonometry", "ripod"]),
                  ("c", ['at', 'lass', 'loser', 'lear', 'ow']),
                  ("u", ['dacity', 'nder', 'nique', 'p', 'ber']),
                ]
  for arg , answer in test_cases:
    try:
      find = MyTrie.find(arg)
      
      if find is not None:
        result  = find.suffixes(arg)

        if result == answer and answer != "AssertionError":
          print("Test Case is Passed !")
        else:
          print("Test case", arg, "Failed")

      else:
        if answer == "AssertionError":
          print("Nice job! Test case {0} correctly raises AssertionError!".format(arg))
        else:
          print("Check your work! Test case {0} should not raise AssertionError!".format(arg))

    except AssertionError:
      if answer == "AssertionError":
        print("Nice job! Test case {0} correctly raises AssertionError!".format(arg))
      else:
        print("Check your work! Test case {0} should not raise AssertionError!".format(arg))

router_test()
