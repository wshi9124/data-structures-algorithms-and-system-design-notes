"""
Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.
You must write an algorithm that runs in O(n) time.

Example 1:
Input: nums = [100,4,200,1,3,2]
Output: 4

Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.

Example 2:
Input: nums = [0,3,7,2,5,8,4,6,0,1]
Output: 9
"""

def longestConsecutive(self, nums):
    """
    :type nums: List[int]
    :rtype:
    """
    # numSet = set(nums)
    # longest = 0

    # for n in numSet:
    #     if n - 1 not in numSet:
    #         current_number = n
    #         current_length = 1
    #         while current_number + 1 in numSet:
    #             current_length += 1
    #             current_number += 1
    #             longest = max(longest, current_length)
    # return longest

    numbers = set(nums)
    longest = 0

    for n in nums:
        if (n - 1) not in numbers:
            length = 1
            while (n + length) in numbers:
                length += 1
            longest = max(longest, length)
    
    return longest


