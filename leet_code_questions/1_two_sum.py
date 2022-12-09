"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]

Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]

Constraints:

2 <= nums.length <= 104
-109 <= nums[i] <= 109
-109 <= target <= 109
Only one valid answer exists.
"""

def twoSum(self, nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    Time complexity: O(n^2)
    Space complexity O(1)
    """
    for i in range(0,len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i,j]

def two_sum_better_way(nums, target):
    """
    Time Complexity: O(n)
    Space Complexity O(n)
    """
    hashmap = {}

    for i in range(0, len(nums)):
        other_number = target - nums[i]
        if other_number in hashmap:
            return [i, hashmap[other_number]]
        else:
            hashmap[nums[i]] = i

numbers = [1,5,7,9,213,3214]
target_number= 214
print(two_sum_better_way(numbers, target_number))