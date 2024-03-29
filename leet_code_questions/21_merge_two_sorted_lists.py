"""
You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.

Example 1:
Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]

Example 2:
Input: list1 = [], list2 = []
Output: []

Example 3:
Input: list1 = [], list2 = [0]
Output: [0]
"""

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mergeTwoLists(list1, list2):
    """
    :type list1: Optional[ListNode]
    :type list2: Optional[ListNode]
    :rtype: Optional[ListNode]
    we create a dummy node so we dont have to worry about edge case of inserting to an empty list 
    Time complexity: l(n)
    Space complexity : O(1)O(1)O(1)
    """
    # dummy = ListNode()
    # tail = dummy 

    # while list1 and list2:
    #     if list1.val < list2.val:
    #         tail.next = list1
    #         list1 = list1.next
    #     else:
    #         tail.next = list2
    #         list2 = list2.next
    #     tail = tail.next    
        
    # if list1:
    #     tail.next = list1
    # elif list2:
    #     tail.next = list2

    # return dummy.next

    dummy = node = ListNode()

    while list1 and list2:
        if list1.val < list2.val:
            node.next = list1
            list1 = list1.next
        else:
            node.next = list2
            list2 = list2.next
        node = node.next
    node.next = list1 or list2

    return dummy.next


# list1 = [1,2,4]
# list2 = [1,3,4]
# print(mergeTwoLists(list1,list2))

#code doesnt work becasue we do not have class for list1 and list2