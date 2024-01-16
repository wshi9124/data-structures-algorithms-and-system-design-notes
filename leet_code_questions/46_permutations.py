"""
Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.

Example 1:
Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

Example 2:
Input: nums = [0,1]
Output: [[0,1],[1,0]]

Example 3:
Input: nums = [1]
Output: [[1]]
"""

def permute(self, nums):
    #result = !len(nums) ex: length 3 = 6 results (3 * 2 * 1)
    result = []

    if len(nums) == 1:
        # nums[:] is a deep copy
        return [nums[:]]
        # .copy() works as well
        return [nums.copy()]
    
    for i in range(len(nums)):
        n = nums.pop(0)
        perms = self.permute(nums)
        #[2,3,1] [3,2,1] we are appending the number we pop into the perm
        for perm in perms:
            perm.append(n)
        result.extend(perms)
        nums.append(n)
    
    return result 



