"""
Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.
There is only one repeated number in nums, return this repeated number.
You must solve the problem without modifying the array nums and uses only constant extra space.

Example 1:
Input: nums = [1,3,4,2,2]
Output: 2

Example 2:
Input: nums = [3,1,3,4,2]
Output: 3
"""
def findDuplicate(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    need to know floyd algorithm 
    """
    #floyed algorithm

    slow, fast = 0, 0 

    while True:
        slow = nums[slow]
        # advances fast twice
        fast = nums[nums[fast]]
        if slow == fast:
            break
    
    slow2 = 0

    while True:
        slow = nums[slow]
        slow2 = nums[slow2]
        if slow == slow2:
            break
    return slow