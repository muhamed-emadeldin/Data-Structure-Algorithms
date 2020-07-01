#!/usr/bin/env python

"""
Given a Matrix mat of N*N size, the task is to complete the function constructLinkedMatrix(), that constructs a 2D linked list representation of the given matrix.
"""

#User function Template for python3

def construct(arr, n):
  
  #defense function
  if arr is None or n == 0:
    return arr

  #basic variables
  head  = None
  tail  = None
  hdown  = None  

  index = 0
  row = 1

  #create loop with n
  for i in range(n):
    for node in arr[i]:
      if head is None and hdown is None:
        head = Node(node)
        head.down = Node(arr[row][index])
        tail = head
        hdown = head.down

      else:
        tail.right = Node(node)
        tail = tail.right

        # if row <= n-1:
        #   tail.down = Node(arr[row][index])
        #   hdown = tail.down
        # else:
        #   tail.down = None
        #   hdown = None

      
      index += 1
      if index == n:
        index = 0
      if hdown is not None:
        print(tail.data,hdown.data, index)
      else:
        print(tail.data,None)
    row += 1
    
      


  return head


#{ 
#  Driver Code Starts
#Initial Template for Python 3

class Node:
    def __init__(self, data):
        self.data = data
        self.right = None
        self.down = None

class LinkedList:
    def __init__(self):
        self.head = None

    def display(self):
        Dp=self.head
        while (Dp):
            Rp = Dp
            while (Rp):
                print(Rp.data, end=" ")
                Rp = Rp.right
            Dp=Dp.down
        print("")

if __name__=='__main__':
    t = int(input())
    while(t>0):
        n = int(input())
        arr = [[0 for i in range(n)] for j in range(n)]
        listto = [int(x) for x in input().strip().split()]
        k=0
        for i in range(n):
            for j in range(n):
                arr[i][j] = listto[k]
                k=k+1

        llist = LinkedList()
        llist.head = construct(arr, n)
        llist.display()
        t=t-1

