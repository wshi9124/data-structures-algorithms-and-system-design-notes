"""
Given the head of a linked list, remove the nth node from the end of the list and return its head.

Example 1:
Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]

Example 2:
Input: head = [1], n = 1
Output: []

Example 3:
Input: head = [1,2], n = 1
Output: [1]
"""

def removeNthFromEnd(self, head, n):
    """
    :type head: ListNode
    :type n: int
    :rtype: ListNode
    """
    # we dont care what the first node is so we set it to zero, but next node has to be head
    dummy = ListNode(0, head)
    left = dummy
    right = head

    while n:
        right = right.next
        n -= 1
    
    while right:
        left = left.next
        right = right.next
    
    #delete node
    left.next = left.next.next

    return dummy.next
    