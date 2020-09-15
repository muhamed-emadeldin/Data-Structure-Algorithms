# Rearrange Array Elements
## How to solve it?
### - first I create a new list with same lenght of input list contains on None item
### - create 2 variables start and end with default value 0, -1
### - make a loop with original list and put 2 condations: if int = 0, int = 2
### - after loop convert only None item in new list to 1 via value of start and end

# Time complexities in worst case: O(n)
### function sort_123() = O(n)
### all variables = O(1)

# Space complexities in worst case: O(n)
### sort_012(input_list) in worst case: O(n)
### all variables = O(1)