"""
Given the root of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

Example 1:
Input: root = [3,9,20,null,null,15,7]
Output: 3

Example 2:
Input: root = [1,null,2]
Output: 2
"""

def maxDepth(self, root) -> int:
    # Recursive DFS
    if not root:
        return 0
    
    return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))

    # Iterative DFS
    stack = [[root,1]]
    result = 0

    while stack: 
        node, depth = stack.pop()

        if node:
            result = max(result, depth)
            stack.append([node.left, depth + 1])
            stack.append([node.right, depth + 1])
        return result

    # Iterative BFS
    q = deque()
    if root:
        q.append(root)
    
    level = 0
    
    while q:
        for i in range(len(q)):
            node = q.popleft()
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        level += 1
    return level
            







