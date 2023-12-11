"""
A path in a binary tree is a sequence of nodes where each pair of adjacent nodes in the sequence has an edge connecting them. A node can only appear in the sequence at most once. Note that the path does not need to pass through the root.
The path sum of a path is the sum of the node's values in the path.
Given the root of a binary tree, return the maximum path sum of any non-empty path.

Example 1:
Input: root = [1,2,3]
Output: 6
Explanation: The optimal path is 2 -> 1 -> 3 with a path sum of 2 + 1 + 3 = 6.

Example 2:
Input: root = [-10,9,20,null,null,15,7]
Output: 42
Explanation: The optimal path is 15 -> 20 -> 7 with a path sum of 15 + 20 + 7 = 42.
"""
def maxPathSum(self, root):
    # list bacuse it makes modifying from recursive function easier
    result = [root.val]

    #return max path sum without split 
    def dfs(root):
        if not root:
            return 0
        
        leftMax = dfs(root.left)
        rightMax = dfs(root.right)
        #need 0 just in case value is negative
        leftMax = max(leftMax, 0)
        rightMax = max(rightMax, 0)
        #compute max path sum with split
        result[0] = max(result[0], root.val + leftMax + rightMax)

        return root.val + max(leftMax, rightMax)
    dfs(root)
    return result[0]





 



