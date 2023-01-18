"""
Given an array of integers arr and an integer k. Find the least number of unique integers after removing exactly k elements.

Example 1:
Input: arr = [5,5,4], k = 1
Output: 1
Explanation: Remove the single 4, only 5 is left.

Example 2:
Input: arr = [4,3,1,1,3,3,2], k = 3

Output: 2
Explanation: Remove 4, 2 and either one of the two 1s or three 3s. 1 and 3 will be left.
"""
def findLeastNumOfUniqueInts(self, arr, k):
    """
    :type arr: List[int]
    :type k: int
    :rtype: int
    """
    hashA = {}

    for number in arr:
        hashA = 1 + hashA.get(number, 0)
    
    values = hashA.values()
    hashA.sort()
    output = len(hashA)

    for value in values:
        k -= value
        if k < 0:
            break
        output -= 1
    return output 