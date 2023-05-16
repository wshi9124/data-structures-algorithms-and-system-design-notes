"""
Given a string s, partition s such that every 
substring of the partition is a  palindrome. Return all possible palindrome partitioning of s.

Example 1:
Input: s = "aab"
Output: [["a","a","b"],["aa","b"]]

Example 2:
Input: s = "a"
Output: [["a"]]
"""

def partition(self, s):
    #backtracking or brute force is main way to solve this
    result = []

    def dfs(i, partition):
        if i == len(s):
            result.append(partition.copy())
            return
        for j in range(i, len(s)):
            if self.isPalindrone(s, i, j):
                # +1 to get correct the off by one error
                partition.append(s[i: j+1])
                dfs(j + 1, partition)
                partition.pop()

    dfs(0, [])
    return result
        


def isPalindrone(self, word, l, r):
    while l < r:
        if word[l] != word[r]:
            return False
        l += 1
        r -= 1
    return True
