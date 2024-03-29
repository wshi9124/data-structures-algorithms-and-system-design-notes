"""
Given the root of a binary tree, return the length of the diameter of the tree.
The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.
The length of a path between two nodes is represented by the number of edges between them.

Example 1:
Input: root = [1,2,3,4,5]
Output: 3
Explanation: 3 is the length of the path [4,2,1,3] or [5,2,1,3].

Example 2:
Input: root = [1,2]
Output: 1
"""

def diameterOfBinaryTree(self, root):
    #global variable
    # result = [0]

    # def dfs(root):
    #     if not root:
    #         return -1
    #     left = dfs(root.left)
    #     right = dfs(root.right)
    #     # +2 because end of node is -1
    #     result[0] = max(result[0], 2 + left + right)

    #     return 1 + max(left, right)
    
    # dfs(root)
    # return result[0]

    result = 0

    def dfs(root):
        # nonlocal keyword is used to work with variables inside nested functions, where the variable should not belong to the inner function
        nonlocal result

        if not root:
            return 0
        left = dfs(root.left)
        right = dfs(root.right)
        result = max(result, left + right)
        return 1 + max(left, right)
    dfs(root)
    return result
