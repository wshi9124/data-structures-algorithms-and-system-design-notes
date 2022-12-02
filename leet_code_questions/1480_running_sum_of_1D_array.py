"""
Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).

Return the running sum of nums.

Examples: 
Input: nums = [1,2,3,4]
Output: [1,3,6,10]
Explanation: Running sum is obtained as follows: [1, 1+2, 1+2+3, 1+2+3+4].

Input: nums = [1,1,1,1,1]
Output: [1,2,3,4,5]
Explanation: Running sum is obtained as follows: [1, 1+1, 1+1+1, 1+1+1+1, 1+1+1+1+1].

Constraints:
1 <= nums.length <= 1000
-10^6 <= nums[i] <= 10^6
"""
"""
Time complexity is O(n) Linear time becasue we perfrom the same number of operations on each element 
Space complexity is O(1) Constant time
"""

def runningSum(nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    for i in range(1,len(nums)):
        nums[i]+= nums[i-1]
    return nums

nums = [1,2,3,4]

print(runningSum(nums))

