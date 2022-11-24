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
print("N1", N1)
N2= Node(20)
N1.next_node = N2
print("N1.next", N1.next_node)

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
        takes O(n) or linear time
        """
        current = self.head
        count = 0
        """
        same as while count != None:
        """
        while current:
            count += 1
            current = current.next_node

        return count

    def add(self, data):
        """ 
        Three ways to add data to the list 
        prepending, appending, inserting 
        below is prepending (adding new node to head of the list)
        constant time operation O(1)
        """
        new_node = Node(data)
        new_node.next_node = self.head
        self.head = new_node

    def search(self, key):
        """
        Search for the first node containing data that matches the key
        Returns the node or None if not found
        Takes O(n) or linear time 
        """
        
        current = self.head

        while current:
            if current.data == key:
                return current
            else:
                current = current.next_node
        return None 
    
    def insert(self, data, index):
        """
        Inserts a new node containing data at index position
        Constant time operation or O(1) but finding the node at the insertion point takes linear time or O(n)
        Overall takes linear time
        """
        if index == 0:
            self.add(data)

        if index > 0:
            new = Node(data)

            position = index
            current = self.head 
        
            while position > 1:
                current = current.next_node
                position -= 1
            
            prev_node = current
            next_node = current.next_node  

            prev_node.next_node = new
            new.next_node = next_node

    """
    There are 2 ways to define remove method 
    1) Provide a key to remove as an arguement 
    2) Provide an index to remove 
    """

    def remove_by_key(self, key):
        current = self.head
        previous = None 
        found = False

        """
        while current != None and found != False (so found = true)  
        """  
        while current and not found:
            if current.data == key and current == self.head:
                found = True
                self.head = current.next_node
            elif current.data == key:
                found = True
                previous.next_node = current.next_node  
            else:
                previous = current
                current= current.next_node
        
        return current


    def __repr__(self):
        """
        Return a string representation of the list 
        Takes O(n) or linear time 
        """
        nodes = []
        current = self.head

        while current:
            if current is self.head:
                nodes.append("[Head: %s]" % current.data)
            elif current.next_node is None:
                nodes.append("[Tail: %s]" % current.data)
            else:
                nodes.append("[%s]" % current.data)
            
            current = current.next_node
        return '-> '.join(nodes)

l = LinkedList() 
N3 = Node(10) 
l.head = N3 
l.add(20)
l.add(15)
l.add(30)
l.insert(1500, 2)
l.remove_by_key(30)
print("size of l", l.size())
print("l", l)
print("search for key", l.search(20))