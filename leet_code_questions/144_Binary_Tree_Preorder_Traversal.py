"""
Given the root of a binary tree, return the preorder traversal of its nodes' values.

Example 1:
Input: root = [1,null,2,3]
Output: [1,2,3]

Example 2:
Input: root = []
Output: []

Example 3:
Input: root = [1]
Output: [1]
"""

def preorderTraversal(self, root):
    """
    :type root: TreeNode
    :rtype: List[int]
    """
    output = []

    def dfs(node):
        if not node:
            return
        output.append(node.val)
        dfs(node.left)
        dfs(node.right)
    
    dfs(root)
    
    return output 
        
    