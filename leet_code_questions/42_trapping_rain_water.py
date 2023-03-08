"""
Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.

Example 1:
Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.

Example 2:
Input: height = [4,2,0,3,2,5]
Output: 9
"""

def trap(self, height: List[int]) -> int:
    output = 0 
    l = 0
    r = len(height) - 1
    maxLeft = height[l]
    maxRight = height[r]

    while l < r:
        if maxLeft < maxRight:
            l += 1
            maxLeft = max(maxLeft, height[l])
            output += maxLeft - height[l]

        else:
            r -= 1
            maxRight = max(maxRight, height[r])
            output += maxRight - height[r]
    
    return output

