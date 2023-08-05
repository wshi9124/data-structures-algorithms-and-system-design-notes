"""
Given an m x n matrix, return all elements of the matrix in spiral order.

Example 1:
Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,2,3,6,9,8,7,4,5]

Example 2:
Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]
"""

def spiralOrder(self, matrix):
    #time O(m * n) space O(1)
    result = []

    left, right = 0, len(matrix[0]) 
    top, bottom = 0, len(matrix)

    while left < right and top < bottom:

        # get every i in the top row
        for i in range(left, right):
            result.append(matrix[top][i])
        top += 1

        # get every i in right col
        for i in range(top, bottom):
            result.append(matrix[i][right - 1])
        right -= 1

        if not (left < right and top < bottom):
            break
        
        # get every i in bottom row
        # left is non inclusive so we need to -1
        for i in range(right -1, left - 1, - 1):
            result.append(matrix[bottom - 1][i])
        bottom -= 1

        # get every i in left col
        for i in range(bottom - 1, top - 1, -1):
            result.append(matrix[i][left])
        left += 1
    
    return result