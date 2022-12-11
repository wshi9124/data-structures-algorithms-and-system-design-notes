"""
Given the head of a singly linked list, reverse the list, and return the reversed list.

Example 1:

Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]

Example 2:
Input: head = [1,2]
Output: [2,1]


Example 3:
Input: head = []
Output: []
"""
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverseListIterative(head):
    """
    :type head: ListNode
    :rtype: ListNode
    iterative solution
    Time complexity O(n)
    Space complexity O(1)
    """
    curr = head
    prev = None 

    while curr:
        #temporary variable to store next when we start our loop
        nxt = curr.next 
        curr.next = prev
        #update pointers 
        prev = curr
        curr = nxt 
    return prev

def reverseListRecursive(self,head):
    """
    :type head: ListNode
    :rtype: ListNode
    iterative solution
    Time complexity O(n)
    Space complexity O(n)
    """
    if not head:
        return None
    
    newHead= head
    if head.next:
        newHead = self.reverseListRecursive(head.next)
        head.next.next = head
    head.next = None 
    return newHead



         