"""
Given the root of a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.

Example 1:
Input: root = [1,2,3,null,5,null,4]
Output: [1,3,4]

Example 2:
Input: root = [1,null,3]
Output: [1,3]

Example 3:
Input: root = []
Output: []
"""

def rightSideView(self, root):
    result = []
    q = collections.deque()

    if root:
        q.append(root)
    
    while q:
        rightNode = None
        for i in range(len(q)):
            node = q.popleft()
            rightNode = node
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        result.append(rightNode.val)
    return result