from linked_list import LinkedList

def merge_sort(linked_list):
    """
    Sorts a linked list in ascending order
    1) Recursively divide the linked list into sublists containing a single node
    2) Repeatedly merge the sublists to produce sorted sublists until one remains 
    3) Returns the sorted linked list 
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
        """
        If the head node of left is None, we're past the tail   
        Add the node from right to merged linked list
        """
        if left_head == None:
            current.next_node = right_head
            right_head = right_head.next_node