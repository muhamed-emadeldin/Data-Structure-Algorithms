"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv


with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)



# initial List
teleNumber = []

def recordDiffTele():
    # get all call and receive numbers with condation "dosen't repeat number"
    for call in calls:
        num1, num2, time, val = call
        if num1 not in teleNumber:
            teleNumber.append(num1)
        if num2 not in teleNumber:
            teleNumber.append(num2)

    # get all call and receive numbers with condation "dosen't repeat number"
    for text in texts:
        num1, num2, time = text
        if num1 not in teleNumber:
            teleNumber.append(num1)
        if num2 not in teleNumber:
            teleNumber.append(num2)

    return "There are {} different telephone numbers in the records.".format(len(teleNumber))

print(recordDiffTele())



"""
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""
