#!/user/bin/env python

def quick_sort(arr):
  sort_all(arr, 0, len(arr)-1)
  return arr

def sort_all(arr, start_index, end_index):
  if end_index <= start_index:
    return 
  
  pivot_index = sort_a_little_bit(arr, start_index, end_index)
  sort_all(arr, start_index, pivot_index-1)
  sort_all(arr, pivot_index+1, end_index)



def sort_a_little_bit(arr, start_index, end_index):
  povit_index = end_index
  povit_value = arr[povit_index]
  left_index = start_index

  while left_index != povit_index:
    item = arr[left_index]

    if item <= povit_value:
      left_index += 1
      continue
    
    #-->swap value of left index with value next item of povit
    arr[left_index] = arr[povit_index - 1]
    #-->shift povit index in next position
    arr[povit_index-1] = povit_value
    #-->shif item position of pivolt position
    arr[povit_index] = item

    povit_index -= 1

  return povit_index

print(quick_sort([5,3,2,1]))
def test_quick_sort():
  test_case = [
                ([5,3,2,1], [1, 2, 3, 5]),
                ([8, 3, 1, 7, 0, 10, 2], [0, 1, 2, 3, 7, 8, 10]),
                ([1, 0], [0, 1]),
              ]

  for args, answer in test_case:
    try:
      result = quick_sort(args)
      if result == answer and answer != "AssertionError":
        print("Test Case is Passed!!!")
      
      else:
        print("Test Case", args, "Faild")
    except AssertionError:
      pass

test_quick_sort()