"""
Given two integer arrays preorder and inorder where preorder is the preorder traversal of a binary tree and inorder is the inorder traversal of the same tree, construct and return the binary tree.

Example 1:
Input: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
Output: [3,9,20,null,null,15,7]

Example 2:
Input: preorder = [-1], inorder = [-1]
Output: [-1]
"""

def buildTree(self, preorder, inorder):
    if not preorder or not inorder:
        return None
    
    #we know that preorder[0] is always going to be the root 
    root = TreeNode(preorder[0])
    #find index of root in inorder
    mid = inorder.index(preorder[0])

    root.left = self.buildTree(preorder[1:mid + 1], inorder[:mid + 1])
    root.right = self.buildTree(preorder[mid + 1:], inorder[mid + 1:])
    return root