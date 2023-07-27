"""
Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.

Example 1:
Input: nums = [3,0,1]
Output: 2
Explanation: n = 3 since there are 3 numbers, so all numbers are in the range [0,3]. 2 is the missing number in the range since it does not appear in nums.

Example 2:
Input: nums = [0,1]
Output: 2
Explanation: n = 2 since there are 2 numbers, so all numbers are in the range [0,2]. 2 is the missing number in the range since it does not appear in nums.

Example 3:
Input: nums = [9,6,4,2,3,5,7,0,1]
Output: 8
Explanation: n = 9 since there are 9 numbers, so all numbers are in the range [0,9]. 8 is the missing number in the range since it does not appear in nums.
"""

def missingNumber(self, nums):
    # O(n) time complexity and space complexity

    numbers = set()

    for n in nums:
        numbers.add(n)
    
    for n in range(len(nums) + 1):
        if n not in numbers:
            return n
    
    # O(n) time complexity, but O(1) space complexity

    result = len(nums)

    for i in range(len(nums)):
        result += (i - nums[i])
    
    return result 
