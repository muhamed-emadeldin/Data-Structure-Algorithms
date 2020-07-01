'''
Exercise 4. Hamming Distance
In information theory, the Hamming distance between two strings of equal length is the number of positions at which the corresponding symbols are different. Calculate the Hamming distace for the following test cases.
'''

def hamming_distance(str1, str2):
  
    """
    Calculate the hamming distance of the two strings

    Args:
       str1(string),str2(string): Strings to be used for finding the hamming distance
    Returns:
       int: Hamming Distance
    """
    
    # TODO: Write your solution here

    # basic variables
    distance = 0

    #check length of two strings is equal or no
    if len(str1) != len(str2):
      return None
    
    for char in range(len(str1)):
      if str1[char] != str2[char]:
        distance += 1

    return distance


def test_hamming_distance():
  test_cases = [
                (("ACTTGACCGGG", "GATCCGGTACA"), 10),
                (("shove", "stove"), 1),
                (("Slot machines", "Cash lost in me"), None),
                (("A gentleman", "Elegant men"), 9),
                (("0101010100011101", "0101010100010001"), 2),
                
               ]
  
  for (args, answer) in test_cases:
    result = hamming_distance(*args)

    if result == answer:
      print("pass")
    else:
      print("Test", args, "faild")

test_hamming_distance()