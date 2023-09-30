"""
You are given an m x n integer matrix matrix with the following two properties:
Each row is sorted in non-decreasing order.
The first integer of each row is greater than the last integer of the previous row.
Given an integer target, return true if target is in matrix or false otherwise.
You must write a solution in O(log(m * n)) time complexity.

Example 1:
Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
Output: true

Example 2:
Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
Output: false
"""
def searchMatrix(self, matrix, target):
    """
    :type matrix: List[List[int]]
    :type target: int
    :rtype: bool
    """

    # rows = len(matrix)
    # column = len(matrix[0])

    # top = 0
    # bottom = row - 1

    # while top <= bottom:
    #     row = (top+bottom) //2
    #     if target > matrix[row][-1]:
    #         top = row + 1
    #     elif target < matrix[row][0]:
    #         bottom = row - 1
    #     else:
    #         break
    # if not (top <= bottom):
    #     return False 
    
    # row = (top+bottom) //2
    # left = 0
    # right = column - 1

    # while left <= right:
    #     mid = (right + left) //2
    #     if matrix[row][mid] == target:
    #         return True
    #     elif matrix[row][mid] > target:
    #         right = mid - 1
    #     else:
    #         left = mid + 1
    # return False
    
    rows, cols = len(matrix), len(matrix[0])

    top, bot = 0, rows - 1

    while top <= bot:
        row = (top + bot) // 2
        if target > matrix[row][-1]:
            top = row + 1
        elif target < matrix[row][0]:
            bot = row - 1
        else:
            break
    
    if not (top <= bot):
        return False

    row = (top + bot) // 2
    l, r = 0, cols - 1

    while l <= r:
        m = (l + r) // 2
        if target < matrix[row][m]:
            r = m - 1
        elif target > matrix[row][m]:
            l = m + 1
        else:
            return True
    return False
