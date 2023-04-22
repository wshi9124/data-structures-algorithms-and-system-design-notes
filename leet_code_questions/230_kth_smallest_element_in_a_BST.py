"""
Given the root of a binary search tree, and an integer k, return the kth smallest value (1-indexed) of all the values of the nodes in the tree.

Example 1:
Input: root = [3,1,4,null,2], k = 1
Output: 1

Example 2:
Input: root = [5,3,6,2,4,null,null,1], k = 3
Output: 3
"""

def kthSmallest(self, root, k):
    #iterative solution
    stack = []
    curr = root

    while curr or stack:
        while curr:
            stack.append(curr.left)
            curr = curr.left
        curr = stack.pop()
        k -= 1
        if k == 0:
            return curr.val
        curr= curr.right
        
    # #DFS
    # a = []
    # if not root: return None
    # stack = [(root)]

    # while stack:
    #     node = stack.pop()
    #     a.append(node.val)
    #     if node.left:
    #         stack.append(node.left)
    #     if node.right:
    #         stack.append(node.right)
    # a.sort()
    # return a[k-1]

    

    

