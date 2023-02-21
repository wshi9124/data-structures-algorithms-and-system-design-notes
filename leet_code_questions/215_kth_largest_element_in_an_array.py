"""
Given an integer array nums and an integer k, return the kth largest element in the array.
Note that it is the kth largest element in the sorted order, not the kth distinct element.
You must solve it in O(n) time complexity.

Example 1:
Input: nums = [3,2,1,5,6,4], k = 2
Output: 5

Example 2:
Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
Output: 4

quick select almost same as quick sort 
"""
def findKthLargestSort(self, nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: int
    O(nlogn) time
    """
    nums.sort()
    return nums[len(nums) - k]

def findKthLargestQuickSelect(self, nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: int
    quick select almost same as quick sort 
    best case O(n) worst case O(n**2)
    average case O(n)
    extra space complexity O(1)
    """
    index = len(nums) - k

    def quickSelect(l,r):
        pivot = nums[r]
        p = l
        for i in range(l,r):
            if nums[i] < pivot:
                nums[p], nums[i] = nums[i], nums[p]
                p += 1
        nums[p], nums[r] = nums[r], nums[p] 

        if p > index: return quickSelect(l, p-1)
        elif p < index: return quickSelect(p+1, r)
        else: return nums[p]
    return quickSelect(0,len(nums-1))