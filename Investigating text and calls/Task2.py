"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv



with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

'''
The solve of question:
1- I will create a dictionary to record phone number as a key and duration as a value.

2- which check if key in the dictionary or no and add duration as a value for the key.
'''

# initial dictionary
dic = {}

# create function to record phone number and value
def recordDic(key1, key2, value):
    if key1 in dic:
        dic[key1] += value
    else:
        dic[key1] = value

    if key2 in dic:
        dic[key2] += value
    else:
        dic[key2] = value

def longestTeleSpent():
    for row in calls:
        num1, num2, time, duration = row
        recordDic(num1, num2, int(duration))

    # grab phone number and its value
    val = dic[max(dic, key=dic.get)]
    key = max(dic, key=dic.get)
    
    return "{} spent the longest time, {} seconds, on the phone during September 2016.".format(key, val)

print(longestTeleSpent())


"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""

