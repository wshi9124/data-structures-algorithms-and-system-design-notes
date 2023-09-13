"""
Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

Example 1:
Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]

Example 2:
Input: nums = [1], k = 1
Output: [1]
 
Constraints:
1 <= nums.length <= 105
-104 <= nums[i] <= 104
k is in the range [1, the number of unique elements in the array].
It is guaranteed that the answer is unique.
"""
def topKFrequent(self, nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: List[int]
    * bucket sort
    """
    # hashmap = {}
    # freq = [[] for i in range(len(nums)+1)]

    # for num in nums:
    #     hashmap[num] = 1 + hashmap.get(num, 0)
    # for number, count in hashmap.items():
    #     freq[count].append(number)
    # # [[], [3], [2], [1], [], [], []]
    
    # result = []

    # for i in range(len(freq)-1, 0, -1):
    #     for num in freq[i]:
    #         result.append[num]
    #         if len(result) == k:
    #             return result

    hashmap = {}
    freq = [[] for i in range(len(nums) + 1)]

    for n in nums:
        hashmap[n] = 1 + hashmap.get(n, 0)
    for n, c in hashmap.items():
        freq[c].append(n)
        # freq[c] += [n]

    result = []
    for i in range(len(freq)-1, 0, -1):
        for n in freq[i]:
            result.append(n)
        if len(result) == k:
            return result

    
