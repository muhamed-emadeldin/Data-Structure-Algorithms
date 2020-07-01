'''
Exercise 1. Reverse Strings
In this first exercise, the goal is to write a function that takes a string as input and then returns the reversed string.

For example, if the input is the string "water", then the output should be "retaw".

While you're working on the function and trying to figure out how to manipulate the string, it may help to use the print statement so you can see the effects of whatever you're trying.
'''

def string_reverser(our_string):
    revers_str = ""
    """
    Reverse the input string

    Args:
       our_string(string): String to be reversed
    Returns:
       string: The reversed string
    """
    
    # TODO: Write your solution here
    # we will loop in len string in range(1, len string) then we will add char with read right to left
    # worst complexity time: O(n)
    for i in range(1, len(our_string)+1):
      revers_str += our_string[-i]

    return revers_str

def teststring_reverser():
  test_cases = [
                ("Mohamed", "demahoM"),
                ("Anas", "sanA"),
                ("!noitalupinam gnirts gnicitcarP", "Practicing string manipulation!"),
                ("3432 :si edoc esuoh ehT", "The house code is: 2343")
               ]
  
  for args, answer in test_cases:
    result = string_reverser(args)

    if result == answer:
      print("pass")
    else:
      print("Test", args, "faild")

teststring_reverser()
