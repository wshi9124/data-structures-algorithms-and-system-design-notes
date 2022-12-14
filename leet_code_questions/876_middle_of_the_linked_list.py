"""
Given the head of a singly linked list, return the middle node of the linked list.
If there are two middle nodes, return the second middle node.

Example 1:
Input: head = [1,2,3,4,5]
Output: [3,4,5]
Explanation: The middle node of the list is node 3.

Example 2:
Input: head = [1,2,3,4,5,6]
Output: [4,5,6]
Explanation: Since the list has two middle nodes with values 3 and 4, we return the second one.
"""

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def middleNodeBestWay(head):
    """
    :type head: ListNode
    :rtype: ListNode
    Time complexity = O(n)
    Space Complexity = O(1)
    """
    turtle = head
    hare = head

    while hare and hare.next:
        turtle = turtle.next
        hare = hare.next.next

    return turtle

def middleNodeBruteForce(head):
    """
    :type head: ListNode
    :rtype: ListNode
    Time complexity = O(n)
    Space Complexity = O(1)
    """
    arr = []

    while head:
        arr.append(head.val)
        head = head.next
    return arr[len(arr)//2]
