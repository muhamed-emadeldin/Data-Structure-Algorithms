#!/usr/bin/env python

"""
Problem Statement
Given an input string, return all permutations of the string in an array.

Example 1:

string = 'ab'
output = ['ab', 'ba']
"""

def recursive(string):
    return permute_srt(string, 0)

def permute_srt(string, index):
  out_list = []

  if index >= len(string):
    return [""]

  sub_str = permute_srt(string, index+1)
  current_char = string[index]

  for item in sub_str:
    for j in range(len(sub_str[0])+1):
      new_str = item[0:j] + current_char + item[j:]
      out_list.append(new_str)

  return out_list


def test_function(test_case):
    string = test_case[0]
    solution = test_case[1]
    output = recursive(string)
    
    output.sort()
    solution.sort()
    
    if output == solution:
        print("Pass")
    else:
        print("Fail")

string = 'ab'
solution = ['ab', 'ba']
test_case = [string, solution]
test_function(test_case)

string = 'abc'
output = ['abc', 'bac', 'bca', 'acb', 'cab', 'cba']
test_case = [string, output]
test_function(test_case)

string = 'abcd'
output = ['abcd', 'bacd', 'bcad', 'bcda', 'acbd', 'cabd', 'cbad', 'cbda', 'acdb', 'cadb', 'cdab', 'cdba', 'abdc', 'badc', 'bdac', 'bdca', 'adbc', 'dabc', 'dbac', 'dbca', 'adcb', 'dacb', 'dcab', 'dcba']
test_case = [string, output]
test_function(test_case)