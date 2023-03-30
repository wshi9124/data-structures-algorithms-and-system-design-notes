"""
Given the head of a linked list, reverse the nodes of the list k at a time, and return the modified list.
k is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a multiple of k then left-out nodes, in the end, should remain as it is.
You may not alter the values in the list's nodes, only nodes themselves may be changed.

Example 1:
Input: head = [1,2,3,4,5], k = 2
Output: [2,1,4,3,5]

Example 2:
Input: head = [1,2,3,4,5], k = 3
Output: [3,2,1,4,5]
"""

def reverseKGroup(self, head, k):
    dummy = ListNode(0, head)
    groupPrev = dummy 
    while True:
        kth = self.getKth(groupPrev, k)
        if not kth:
            break
        groupNext = kth.next
        #reverse groups
        prev, curr = kth.next, groupPrev.next
        while curr != groupNext:
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp
        #becasue kth is the last node in our group we now want it to be the first node in our group
        temp = groupPrev.next
        groupPrev.next = kth
        groupPrev = temp
    return dummy.next
    

def getKth(self, curr, k):
    while curr and k > 0:
        curr = curr.next
        k -= 1
    return curr