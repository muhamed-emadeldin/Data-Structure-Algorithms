'''
The goal of this exercise is to write some code to determine if two strings are anagrams of each other.

An anagram is a word (or phrase) that is formed by rearranging the letters of another word (or phrase).

For example:

"rat" is an anagram of "art"
"alert" is an anagram of "alter"
"Slot machines" is an anagram of "Cash lost in me"
Your function should take two strings as input and return True if the two words are anagrams and False if they are not.

You can assume the following about the input strings:

No punctuation
No numbers
No special characters
'''

def anagram_checker(str1, str2):
    new_str1 = sorted(str1.lower().strip().replace(" ", ""))
    new_str2 = sorted(str2.lower().strip().replace(" ", ""))
    """
    Check if the input strings are anagrams of each other

    Args:
       str1(string),str2(string): Strings to be checked
    Returns:
       bool: Indicates whether strings are anagrams
    """
    
    # TODO: Write your solution here
    if len(new_str1) != len(new_str2):
      return False

    for i in range(len(new_str1)):
      if new_str1[i] != new_str2[i]:
        return False
    
    return True

def testanagram_checker():
  test_cases = [
                (("Moha med", "demah oM"), True),
                (("rat", "art"), True),
                (("alert", "alter"), True),
                (("Slot machines", "Cash lost in me"), True),
                (("water", "waiter"), False),
                (("Dormitory", "Dirty room"), True),
                (('A gentleman','Elegant men'), False),
                (("Time and tide wait for no man", "Notified madman into water"), True),
                
               ]
  
  for (args, answer) in test_cases:
    result = anagram_checker(*args)
    if result == answer:
      print("pass")
    else:
      print("Test", args, "faild")

testanagram_checker()