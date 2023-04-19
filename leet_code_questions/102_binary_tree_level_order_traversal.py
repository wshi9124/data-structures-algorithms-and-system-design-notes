"""
Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).

Example 1:
Input: root = [3,9,20,null,null,15,7]
Output: [[3],[9,20],[15,7]]
Example 2:

Input: root = [1]
Output: [[1]]
Example 3:

Input: root = []
Output: []
"""

def levelOrder(self, root):
    """
    :type root: TreeNode
    :rtype: List[List[int]]
    Time complexity : O(n)
    Space complexity O(n)
    """
    result = []
    q = collections.deque()

    if root:
        q.append(root)
    
    while q:
        val = []
        for i in range(len(q)):
            node = q.popleft()
            val.append(node.val)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        result.append(val)
    return result
        