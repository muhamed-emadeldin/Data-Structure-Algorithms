#create a Node Class
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


#create Linked list class
class LinkedList:
    def __init__(self, head):
        self.head = head

    def append(self, value):
        if self.head is None:
            self.head = Node(value)
            return

        node = self.head

        while node.next is not None:
            node = node.next
            return
        
        node.next = Node(value)

    def to_list(self):
        out_list = []
        if self.head is None:
            return None
        
        node = self.head

        while node:
            out_list.append(int(str(node.value)))
            node = node.next
        
        return out_list



#create merge function that takes 2 args
def merge(list1, list2):
    merge = LinkedList(None)
    if list1 is None:
        return list2
    
    if list2 is None:
        return list2

    llist1 = list1.head
    llist2 = llist2.head

    while llist1 is not None or llist2 is not None:
        if llist1 is None:
            merge.append(llist2)
            llist2 = llist2.next

        elif llist2 is None:
            merge.append(llist1)
            llist1 = llist1.next

        elif llist1.value <= llist2.value:
            merge.append(llist1)
            llist1 = llist1.next

        else:
            merge.append(llist2)
            llist2 = llist2.next

        return merge

# create NestedLinkedList calss
class NestedLinkedList(LinkedList):
    def flatten(self):
        return self._flatten(self.head)

    def _flatten(self, node):
        if node.next is None:
            return merge(node.value, None)

        return merge(node.value, self._flatten(node.next))

# First Test scenario
''' Create a simple LinkedList'''
linked_list = LinkedList(Node(1)) # <-- Notice that we are passing a Node made up of an integer
linked_list.append(3) # <-- Notice that we are passing a numerical value as an argument in the append() function here 
linked_list.append(5)

''' Create another simple LinkedList'''
second_linked_list = LinkedList(Node(2))
second_linked_list.append(4)

''' Create a NESTED LinkedList, where each node will be a simple LinkedList in itself'''
nested_linked_list = NestedLinkedList(Node(linked_list)) # <-- Notice that we are passing a Node made up of a simple LinkedList object
nested_linked_list.append(second_linked_list) # <-- Notice that we are passing a LinkedList object in the append() function here