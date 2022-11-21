"""
Linked List- linear data structure where each element in the list is contained in a separate object called a node
"""

"""
Node- models 2 pieces of information, an individual item of the data we want to store and a reference to the next node in the list 
The first node of a linked list is the head and the last node is the tail
linked list only makes a reference to the head although in some implementations they also keep reference to the tail as well
Self Referencial Object- definition of node is includes the node itself
""" 

"""
2 Types of Linked Lists
1) Singly Linked List- each node stores a reference to the next node in the list  
2) Doubly Linked List- each node stores a reference to both the node before and after the list
"""

class Node:
    """
    An object for storing a single node to a linked list.
    Models two attributes- data and the link to the next node in the list 
    """

    data = None
    next_node = None 

    def __init__(self, data):
        self.data = data

    def __repr__(self):
        return "<Node data: %s>" %self.data 

N1= Node(10)
print(N1)
N2= Node(20)
N1.next_node = N2
print(N1.next_node)

class LinkedList:
    """
    Makes sure new list is alwasy empty
    Singly Linked List
    """
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head == None

    def size(self):
        """
        Returns the number of nodes in the list 
        """
        current = self.head
        count= 0
        """
        same as while count != None:
        """
        while current:
            count += 1
            current = current.next_node

