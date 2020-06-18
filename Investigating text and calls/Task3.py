#!/usr/bin/env python
"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
import re


with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

'''
The solve of question one:
1 - we need to know if calling from Bangalore we will grab the receiving telephone
2-  I will to create a list to record all codes area and mobile prefixes
3- Return the sorted value of CallBangalore.
'''

'''
The solve of question two:
1- I will grab all numbers from Bangalore and grab all calling from Bangalore and calculate percentage between them
'''


# initial basic variables
codeArea = []
callBang = 0
allBang  = 0 


def checkCallNumber(num2):
  global callBang

  fixedLinePattern  = re.search(r"^\((\d*)\)(\d*)$", num2)
  mobilePattern     = re.search(r"^(\d{1})(\d{3})(\d*)(\s)([\d]*)$", num2)
  telePattern       = re.search(r"^(\d{3})([\d]*)$", num2)

  # check if this number is fixted line
  if fixedLinePattern is not None and fixedLinePattern[1].startswith("0"):
    codeArea.append(fixedLinePattern[1])

  if mobilePattern is not None:
    if mobilePattern[1] == "7" or mobilePattern[1] == "8" or mobilePattern[1] == "9" and mobilePattern[4] == " ":
      result = mobilePattern[1] + mobilePattern[2]
      codeArea.append(result)

  if num2.startswith("140"):
    codeArea.append(num2.startswith("140"))

  if num2.startswith("(080)"):
      callBang += 1
  

# create function to read the csv file
def callBangalore():
  global allBang

  for  row in calls:
    num1, num2, time, val = row
    
    if num1.startswith("(080)"):
      checkCallNumber(num2)
      allBang += 1

  answerQuize1 = "The numbers called by people in Bangalore have codes:\n" + "\n".join([i for i in sorted(set(codeArea))])

  answerQuize2 = "{:.2f}% percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore.".format((callBang/allBang) * 100)

  # The solution for question one

  return answerQuize1 + "\n" + "\n" + answerQuize2


print(callBangalore())
  

"""
TASK 3:
(080) is the area code for fixed line telephones in Bangalore.
Fixed line numbers include parentheses, so Bangalore numbers
have the form (080)xxxxxxx.)



Part A: Find all of the area codes and mobile prefixes called by people
in Bangalore. 
 - Fixed lines start with an area code enclosed in brackets. The area
   codes vary in length but always begin with 0.

 - Mobile numbers have no parentheses, but have a space in the middle
   of the number to help readability. The prefix of a mobile number
   is its first four digits, and they always start with 7, 8 or 9.
 - Telemarketers' numbers have no parentheses or space, but they start
   with the area code 140.

Print the answer as part of a message:
"The numbers called by people in Bangalore have codes:"
 <list of codes>
The list of codes should be print out one per line in lexicographic order with no duplicates.

Part B: What percentage of calls from fixed lines in Bangalore are made
to fixed lines also in Bangalore? In other words, of all the calls made
from a number starting with "(080)", what percentage of these calls
were made to a number also starting with "(080)"?

Print the answer as a part of a message::
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
The percentage should have 2 decimal digits
"""

