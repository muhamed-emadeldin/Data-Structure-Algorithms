#! /usr/env/bin python

from collections import defaultdict
#create TrieNode class
class TrieNode:
    def __init__(self):
        self.is_word = False
        self.children = {}

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        current_node = self.root
        for chr in word:
            if not chr in current_node.children:
                current_node.children[chr] = TrieNode()
            current_node = current_node.children[chr]

        current_node.is_word = True

    def search(self, word):
        current_node = self.root
        for chr in word:
            if not chr in current_node.children:
                return False
            current_node = current_node.children[chr]
        return current_node.is_word

    def __str__(self):
        current_node = self.root
        s = ""
        
        while current_node.children:
            for k in current_node.children.keys():
                current_node = current_node.children[k]
                s += str(k)
        return s

trie = Trie()
trie.insert("car")
print(trie)
