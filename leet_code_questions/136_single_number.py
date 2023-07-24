"""
Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.
You must implement a solution with a linear runtime complexity and use only constant extra space.

Example 1:
Input: nums = [2,2,1]
Output: 1

Example 2:
Input: nums = [4,1,2,1,2]
Output: 4

Example 3:
Input: nums = [1]
Output: 1
"""
# bit manipulation 

def singleNumber(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    bit manipulation XOR
    2 ^ 0 = 2
    2 ^ 2 = 0
    """
    # hashmap = {}

    # for num in nums:
    #     hashmap[num] = 1 + hashmap.get(num, 0)

    # for key in hashmap:
    #     if hashmap[key] == 1:
    #         return key

    #O(1) memory solution
    # XOR or exclusive or
    # ex: 0 ^ 0 = 0, 1 ^ 0 = 1
    # if 2 numbers are same you get 0 if they are different you add the 2 numbers up 
    result = 0

    for n in nums:
        result = n ^ result
    return result
    
