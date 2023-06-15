"""
There is a new alien language that uses the English alphabet. However, the order among the letters is unknown to you.
You are given a list of strings words from the alien language's dictionary, where the strings in words are 
sorted lexicographically by the rules of this new language.
Return a string of the unique letters in the new alien language sorted in lexicographically increasing order by the new language's rules. If there is no solution, return "". If there are multiple solutions, return any of them.

Example 1:
Input: words = ["wrt","wrf","er","ett","rftt"]
Output: "wertf"

Example 2:
Input: words = ["z","x"]
Output: "zx"

Example 3:
Input: words = ["z","x","z"]
Output: ""
Explanation: The order is invalid, so return "".
"""

def alienOrder(self, words):
    # topological sort  
    # if there is a cycle we return ""

    adj = {c: set() for w in words for c in w}

    for i in range(len(words) - 1):
        w1, w2 = words[i], words[i + 1]
        minLen = min(len(w1), len(w2))
        # if prefix of w1 and w2 are the same but w2 is longer 
        if w1[:minLen] == w2[:minLen] and len(w1) > len(w2):
            return ""
        for j in range(minLen):
            #we want the first different character
            if w1[j] != w2[j]:
                adj[w1[j]].add(w2[j])
                break
    
    visit = {} #False = visited, True = visited and current path
    result = [] #list initially then we join and reverse at the end 

    def dfs(c):
        # loop detection if c in vist it will return True
        if c in visit:
            return visit[c]
        visit[c] = True
        for nei in adj[c]:
            if dfs(nei):
                return True
        visit[c] = False
        result.append(c)
    
    for c in adj:
        if dfs(c):
            return ""

    result.reverse()
    return "".join(result)        


