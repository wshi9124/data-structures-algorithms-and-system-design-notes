"""
Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.
The overall run time complexity should be O(log (m+n)).

Example 1:
Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.

Example 2:
Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.50000
Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.
"""
def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
    a, b = nums1, nums2
    total = len(a) + len(b) 
    half = total //2

    if len(a) > len(b):
        a,b = b,a
    
    l, r = 0, len(a) -1
    while True:
        i = (l +r)//2 #a
        j = half - i - 2 #b
        #float infinity for edge case if none of the numbers are in the first array
        aLeft = a[i] if i >= 0 else float("-infinity")
        aRight = a[i+1] if i+1 < len(a) else float("infinity")
        bLeft = b[j] if j >= 0 else float("-infinity")
        bRight = b[j+1] if j+1 < len(b) else float("infinity")

        if aLeft <= bRight and bLeft <= aRight:
            #odd
            if total % 2 != 0:
                return min(aRight, bRight)
            #even
            return (max(aLeft, bLeft) + min(aRight, bRight)) /2
        elif aLeft > bRight:
            r = i -1
        else:
            l = i + 1



    
