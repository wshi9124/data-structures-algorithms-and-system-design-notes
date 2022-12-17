"""
Given the root of a binary tree, determine if it is a valid binary search tree (BST).

A valid BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.
 
Example 1:
Input: root = [2,1,3]
Output: true
Example 2:

Input: root = [5,1,4,null,null,3,6]
Output: false
Explanation: The root node's value is 5 but its right child's value is 4.
"""

def isValidBST(root):
    """
    :type root: TreeNode
    :rtype: bool
    recursive function
    Both time complexity and space complexity is O(n)
    """
    def valid_using_dfs(node, left, right):
        #its still valid if its empty tree
        if not node:
            return True 

        if not (node.val > left and node.val < right):
            return False 
        
        if valid_using_dfs(node.left, left, node.val) == True and valid_using_dfs(node.right, node.val, right) == True:
            return True 
    
    valid_using_dfs(root, float("-inf"), float("inf"))
    