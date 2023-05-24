"""
You are given an m x n binary matrix grid. An island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.
The area of an island is the number of cells with a value 1 in the island.
Return the maximum area of an island in grid. If there is no island, return 0.

Example 1:
Input: grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]
Output: 6
Explanation: The answer is not 11, because the island must be connected 4-directionally.

Example 2:
Input: grid = [[0,0,0,0,0,0,0,0]]
Output: 0
"""

def maxAreaOfIsland(self, grid):
    maxArea = 0
    row = len(grid)
    cols = len(grid[0])

    for r in range(row):
        for c in range(cols):
            if grid[r][c] == 1:
                area = self.dfs(grid, r, c)
                maxArea = max(maxArea, area)
    return maxArea


def dfs(self, grid, r, c):
    if r < 0 or c < 0 or r >= len(grid) or c >= len(grid[0]) or grid[r][c] != 1:
        return 0
    grid[r][c] = 0
    return 1 + self.dfs(grid, r + 1, c) + self.dfs(grid, r - 1, c) + self.dfs(grid, r, c + 1) + self.dfs(grid, r, c - 1)