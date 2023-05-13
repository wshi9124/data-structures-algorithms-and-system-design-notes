"""
Given an integer array nums that may contain duplicates, return all possible 
subsets (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.

Example 1:
Input: nums = [1,2,2]
Output: [[],[1],[1,2],[1,2,2],[2],[2,2]]

Example 2:
Input: nums = [0]
Output: [[],[0]]
 
"""

def subsetsWithDup(self, nums):
     # time complexity n * 2**n

    result = []
    nums.sort()

    def backTrack(i, subset):
        if i == len(nums):
            result.append(subset.copy())
            # result.append(subset[::]) works as well
            return

        # all subsets that include nums[i]
        subset.append(nums[i])
        backTrack(i + 1, subset)
        subset.pop()

        # all subsets that dont include nums[i]
        while i + 1 < len(nums) and nums[i + 1] == nums[i]:
            i += 1
        backTrack(i+1, subset)
    backTrack(0, [])
    return result 