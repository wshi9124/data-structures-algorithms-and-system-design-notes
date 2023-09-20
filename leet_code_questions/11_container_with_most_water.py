"""
You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).
Find two lines that together with the x-axis form a container, such that the container contains the most water.
Return the maximum amount of water a container can store.
Notice that you may not slant the container.

Example 1:
Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.

Example 2:
Input: height = [1,1]
Output: 1
"""

def maxarea(self, height):
    """
    :type height: List[int]
    :rtype: int
    """
    # left = 0
    # right = len(height) -1 
    # max_area = 0

    # while left < right:
    #     width = right - left
    #     area = width * min(height[left], height[right])
    #     max_area = max(max_area, area)
    #     if height[right] > height[left]:
    #         left +=1
    #     else:
    #         right-=1
    # return max_area

    # l = 0
    # r = len(height) - 1
    # maxArea = 0

    # while l < r:
    #     width = r - l
    #     area = min(height[l], height[r]) * width
    #     maxArea = max(maxArea, area)
    #     if height[l] < height[r]:
    #         l += 1
    #     else:
    #         r -= 1
    # return maxArea

    l = 0
    r = len(height) - 1
    volume = 0

    maxLeft = height[l]
    maxRight = height[r]
    
    while l < r:
        if maxLeft < maxRight:
            l += 1
            maxLeft = max(maxLeft, height[l])
            volume += maxLeft - height[l]
        else:
            r -= 1
            maxRight = max(maxRight, height[r])
            volume += maxRight - height[r]
    return volume


