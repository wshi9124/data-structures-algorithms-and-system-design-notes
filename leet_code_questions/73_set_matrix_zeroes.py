"""
Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's.
You must do it in place.

Example 1:
Input: matrix = [[1,1,1],[1,0,1],[1,1,1]]
Output: [[1,0,1],[0,0,0],[1,0,1]]

Example 2:
Input: matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
Output: [[0,0,0,0],[0,4,5,0],[0,3,1,0]]
"""

def setZeroes(self, matrix):
    # O(1) solution

    rows, cols = len(matrix), len(matrix[0])
    # check if first row is zero or not 
    rowZero = False

    #determine which rows/ cols need to be zero
    for r in range(rows):
        for c in range(cols):
            if matrix[r][c] == 0:
                matrix[0][c] = 0
                if r > 0:
                    matrix[0][r] = 0
                else:
                    rowZero = True

    for r in range(rows):
        for c in range(cols):
            if matrix[0][c] == 0 or matrix[r][0] == 0:
                

sca