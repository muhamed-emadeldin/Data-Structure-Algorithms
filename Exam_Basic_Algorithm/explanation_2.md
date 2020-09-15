# Search in a Rotated Sorted Array
## How to solve it?
### - Use divide and conquer algorithm
### - get a good pivot
### - create a function called binary search with 3 arguments (target, start, end)


# Time complexities in worst case: O(log(n))
### function rotated_array_search(input_list, number) = O(log(n))
### function findPivot(arr, start, end) = O(log(n))
### function binary_search_tree(arr, target, start, end) = O(log(n))
### all variables = O(1)


# Space complexities in worst case: O(n)
### rotated_array_search(input_list, number) in worst case: O(n)
### findPivot(input_list, 0, n-1) in worst case: O(n)
### binary_search_tree(arr, target, start, end) in worst case: O(n)
### all variables = O(1)
