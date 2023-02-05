from linked_list import LinkedList

def merge_sort(linked_list): 
    """
    Sorts a linked list in ascending order
    1) Recursively divide the linked list into sublists containing a single node
    2) Repeatedly merge the sublists to produce sorted sublists until one remains 
    3) Returns the sorted linked list 

    Runs in O(kn log n) becasue of split function but ideally merge sort runs in O(n log n) or quasilinear or log linear runtime
    """

    if linked_list.size() == 1:
        return linked_list
    elif linked_list.head is None:
        return linked_list
    
    left_half, right_half = split(linked_list)
    left = merge_sort(left_half)
    right = merge_sort(right_half)

    return merge(left, right)

def split(linked_list):
    """
    Divide the unsorted list at midpoint into sub linked lists
    """

    if linked_list == None or linked_list.head == None:
        left_half = linked_list 
        right_half = None 

        return left_half, right_half
    
    else: 
        size = linked_list.size()
        mid = size//2
        
        """
        -1 becasue we get size however index always starts at 0
        However we are traversing the list here so there is a O(k log n) cost here
        """
        mid_node = linked_list.node_at_index(mid-1)

        left_half = linked_list
        right_half = LinkedList()
        right_half.head = mid_node.next_node
        """
        Server tail of mid node  
        """
        mid_node.next_node = None

        return left_half, right_half

def merge(left, right):
    """
    Merges two linked lists, sorting by data in nodes
    Returns a new merged list 
    Runs in O(n) or linear time 
    """

    # Create a new linked list that contains nodes from merging left and right 
    merged = LinkedList()
    # Add a fake head to be discarded later
    merged.add(0)
    # set current to the head of the linked list
    current = merged.head  
    # Obtain head nodes for left and right of linked list
    left_head = left.head
    right_head = right.head 
    # Iterate over left and right until we reach the tail node of either 
    while left_head or right_head:
        # If the head node of left is None, we're past the tail   
        # Add the node from right to merged linked list
        if left_head == None:
            current.next_node = right_head
            # Call next on right to set loop condition to false 
            right_head = right_head.next_node    
        # If the head node of right is None, we're past the tail
        # Add the tail node from left to merged linked list 
        elif right_head == None:
            current.next_node = left_head
            # call next on left to set loop condition to false 
            left_head = left_head.next_node
        else:
            # Not at either tail node
            # Obtain node data to perform comparison operations
            left_data = left_head.data
            right_data = right_head.data
            # If data on left is less than right, set current to left node 
            if left_data < right_data:
                current.next_node = left_head
                # Move left head to next node 
                left_head = left_head.next_node 
            # If data on left is greater than right, set current to right node 
            else:
                current.next_node = right_head
                #Move right head to next node 
                right_head = right_head.next_node 
        # Move current to next node 
        current = current.next_node
    
    # Discard fake head and set first merged node as head
    head = merged.head.next_node
    merged.head = head

    return merged

l = LinkedList()
l.add(20)
l.add(5)
l.add(96)
l.add(27)
l.add(10)
l.add(15)
l.add(45)
print("Linked List", l)
print("Sorted Linked List", merge_sort(l))