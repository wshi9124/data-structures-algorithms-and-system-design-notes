"""
Given an m x n board of characters and a list of strings words, return all words on the board.
Each word must be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once in a word.

Example 1:
Input: board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]], words = ["oath","pea","eat","rain"]
Output: ["eat","oath"]

Example 2:
Input: board = [["a","b"],["c","d"]], words = ["abcb"]
Output: []
"""

class TrieNode:
    def __init__(self):
        self.children = {}
        self.end = False
        self.refs = 0
    
    def addWord(self, word):
        curr = self
        curr.refs += 1
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
            curr.refs += 1
        curr.end = True 
    
    # Needed for efficiency to prune words or remove words from the tree
    def removeWord(self, word):
        curr = self
        curr.refs -= 1
        for c in word:
            if c in curr.children:
                curr = curr.children[c]
                curr.refs -= 1
            
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()

        for w in words:
            root.addWord(w)

        rows, cols = len(board), len(board[0])
       
        #use result set so that we don't have duplicate answers
        #use path set so that we dont revisit the same position twice
        result, path = set(), set()
        
        #use node instead of index unlike word search I
        def dfs(r, c, node, word):
            if(r < 0 or c < 0 or
            r >= rows or c >= cols or
            board[r][c] not in node.children or
            (r,c) in path or
            node.children[board[r][c]].refs < 1 
            ): 
                return

            path.add((r,c))
            node = node.children[board[r][c]]
            word += board[r][c]
            if node.end == True:
                node.end = False
                result.add(word)
                root.removeWord(word)
            dfs(r + 1, c, node ,word)
            dfs(r - 1, c, node ,word)
            dfs(r, c + 1, node ,word)
            dfs(r, c - 1, node ,word)

            path.remove((r,c))
        
        for r in range(rows):
            for c in range(cols):
                dfs(r, c, root, "")
        
        return list(result)
