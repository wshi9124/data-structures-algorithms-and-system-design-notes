"""
Given an m x n grid of characters board and a string word, return true if word exists in the grid.
The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.

Example 1:
Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
Output: true
Example 2:

Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SEE"
Output: true
Example 3:

Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCB"
Output: false
"""

def exist(self, board, word):
    rows, cols = len(board), len(board[0])
    #use set so that we dont revisit the same position twice
    path = set()

    #i is current character within our word
    def dfs(r, c, i):
        if i == len(word):
            return True

        if (r < 0 or c < 0 or
        r >= rows or c >= cols or
        word[i] != board[r][c] or
        (r,c) in path): return False

        path.add((r, c))

        result = (
            dfs(r + 1 , c ,i + 1) or
            dfs(r - 1, c ,i + 1) or
            dfs(r , c + 1 ,i + 1) or
            dfs(r , c - 1 ,i + 1))
        
        path.remove((r,c))
        return result

    for r in len(rows):
        for c in len(cols):
            if dfs(r, c, 0): return True
    return False

    # O(n * m * dfs) 
    # dfs= 4^len(word)