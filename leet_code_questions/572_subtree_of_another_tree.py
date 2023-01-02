"""
Given the roots of two binary trees root and subRoot, return true if there is a subtree of root with the same structure and node values of subRoot and false otherwise.

A subtree of a binary tree tree is a tree that consists of a node in tree and all of this node's descendants. The tree tree could also be considered as a subtree of itself.

Example 1:
Input: root = [3,4,5,1,2], subRoot = [4,1,2]
Output: true

Example 2:
Input: root = [3,4,5,1,2,null,null,null,null,0], subRoot = [4,1,2]
Output: false
"""

def isSubtree(self, root, subRoot):
    """
    :type root: TreeNode
    :type subRoot: TreeNode
    :rtype: bool
    """
    if root == None: 
        return False
    if subRoot == None:
        return True 
    
    if root.val == subRoot.val:
        self.helper_is_same_tree(root, subroot)

    return self.helper_is_same_tree(root.left, subRoot) or self.helper_is_same_tree(root.right, subRoot)

def helper_is_same_tree(self, s, t):
    if s == None and t == None:
        return True
    
    if s and t and s.val == t.val:
        return (self.helper_is_same_tree(s.left, t.left) and self.helper_is_same_tree(s.right, t.right))
    return False 
