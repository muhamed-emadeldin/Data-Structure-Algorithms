#!/usr/bin/env python

'''
Problem Statement
You have been given an array containg numbers. Find and return the largest sum in a contiguous subarray within the input array.
'''

def max_sum_subarray(arr):
    
    current_sum = arr[0] # `current_sum` denotes the sum of a subarray
    max_sum = arr[0]     # `max_sum` denotes the maximum value of `current_sum` ever
    
    # Loop from VALUE at index position 1 till the end of the array
    for element in arr[1:]:
        
        '''
        # Compare (current_sum + element) vs (element)
        # If (current_sum + element) is higher, it denotes the addition of the element to the current subarray
        # If (element) alone is higher, it denotes the starting of a new subarray
        '''
        
        current_sum = max(current_sum + element, element)
        print(current_sum, element)
        
        # Update (overwrite) `max_sum`, if it is lower than the updated `current_sum`
        # print(max_sum)
        max_sum = max(current_sum, max_sum)   
    
    return max_sum


print(max_sum_subarray([-12, 15, -13, 14, -1, 2, 1, -5, 4]))