"""
Given a binary tree, determine if it is height-balanced
A height-balanced binary tree is a binary tree in which the depth of the two subtrees of every node never differs by more than one.


Example 1:
Input: root = [3,9,20,null,null,15,7]
Output: true
Example 2:


Input: root = [1,2,2,3,3,null,null,4,4]
Output: false
Example 3:

Input: root = []
Output: true
"""

def isBalanced(self, root):
    # def dfs(root):
    #     if not root: return [True, 0]
    
    #     left, right = dfs(root.left), dfs(root.right)
    #     #need to check if left and right is balanced (true)
    #     balanced = left[0] and right[0] and abs(left[1] - right[1]) <= 1

    #     return [balanced, 1 + max(left[1], right[1])]
    
    # return dfs(root)[0]

    def dfs(root):
        if not root:
            return [True, 0]
        
        left, right = dfs(root.left), dfs(root.right)
        balanced = left[0] and right[0] and abs(left[1] - right[1]) <= 1
        return [balanced, 1 + max(left[1], right[1])]
    
    return dfs(root)[0]


