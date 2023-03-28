"""
Given an integer array nums of unique elements, return all possible 
subsets (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.

Example 1:
Input: nums = [1,2,3]
Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]

Example 2:
Input: nums = [0]
Output: [[],[0]]
"""

def subsets(self, nums):
    """
    Not permutation so we do not want duplicates 
    * so no [2,1]
    """

    result = []

    def dfs(i, subset):
        if i >= len(nums):
            result.append(subset)
            return
        dfs(i+1, subset + [nums[i]])
        dfs(i+1, subset)

    dfs(0, [])
    return result

    # result = []
    # subset = []

    # def dfs(i):
    #     if i >= len(nums):
    #         #need .copy because subset is going to be modified
    #         result.append(subset.copy())
    #         return
    #     #decision to include nums[i]
    #     subset.append(nums[i])
    #     dfs(i+1)
    #     # decision not to include nums[i]
    #     subset.pop()
    #     dfs(i+1)
    # dfs(0)
    # return result
        