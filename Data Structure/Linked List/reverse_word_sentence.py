'''
Exercise 3. Reverse the words in sentence
Given a sentence, reverse each word in the sentence while keeping the order the same!
'''



def word_flipper(our_string):
  
    """
    Flip the individual words in a sentence

    Args:
       our_string(string): String with words to flip
    Returns:
       string: String with words flipped
    """
    
    # TODO: Write your solution here
    new_str = our_string.split(" ")

    for i in range(len(new_str)):
      new_str[i] = new_str[i][::-1]
    return " ".join(new_str)
    
  


def testword_flipper():
  test_cases = [
                ("Mohamed", "demahoM"),
                ("Anas", "sanA"),
                ("retaw", "water"),
                ("sihT si na elpmaxe", "This is an example"),
                ("sihT si eno llams pets rof ...", "This is one small step for ..."),
               ]
  
  for args, answer in test_cases:
    result = word_flipper(args)

    if result == answer:
      print("pass")
    else:
      print("Test", args, "faild")

testword_flipper() 