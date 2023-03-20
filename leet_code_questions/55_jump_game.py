"""
You are given an integer array nums. You are initially positioned at the array's first index, and each element in the array represents your maximum jump length at that position.
Return true if you can reach the last index, or false otherwise.

Example 1:
Input: nums = [2,3,1,1,4]
Output: true
Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.

Example 2:
Input: nums = [3,2,1,0,4]
Output: false
Explanation: You will always arrive at index 3 no matter what. Its maximum jump length is 0, which makes it impossible to reach the last index.
"""

def canJump(self, nums):
    # start at the second to last index, end at last index, -1 index everytime
    # nums-2 because you dont need to know last number
    goal = len(nums) - 1 

    for i in range(len(nums)-2, -1, -1):
        if i + nums[i] >= goal:
            goal = i
    return True if goal == 0 else False
