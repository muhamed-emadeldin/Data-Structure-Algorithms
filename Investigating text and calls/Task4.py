"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""


"""

TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.

"""

import csv

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)


'''
create a function that records all phone numbers out calling from telemarketers in a list and search them in the text CSV file if I found the number in the text CSV file I will remove it from the list and in the end I will return with the numbers that are still in the list.
'''

#initial basic variables
sendCall    = []
receiveCall = []
result      = []

def sendReceiveText():
    # 
    for row in calls:
        num1, num2, time, val = row
        # create a list with outing calling with no duplicate numbers
        if not num1 in sendCall:
            sendCall.append(num1) 
       
        # create a list with incoming calling with no duplicate numbers
        if not num2 in receiveCall:
            receiveCall.append(num2)
    
    # create a new list called result to append all numbers which don't found in incoming calling
    for call in sendCall:
        if not call in receiveCall:
            if not call in result:
                result.append(call)
    # remove all numbers from the result list which sends a text or receive text
    for text in texts:
        txt1, txt2, time = text
        for call in result:
            if txt1 == call or txt2 == call:
                result.remove(call)

    return "These numbers could be telemarketers: \n" + "\n".join([i for i in sorted(result)]) 

print(sendReceiveText())