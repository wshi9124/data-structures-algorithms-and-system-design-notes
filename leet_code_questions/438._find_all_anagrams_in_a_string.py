"""
Given two strings s and p, return an array of all the start indices of p's anagrams in s. You may return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

Example 1:
Input: s = "cbaebabacd", p = "abc"
Output: [0,6]
Explanation:
The substring with start index = 0 is "cba", which is an anagram of "abc".
The substring with start index = 6 is "bac", which is an anagram of "abc".

Example 2:
Input: s = "abab", p = "ab"
Output: [0,1,2]
Explanation:
The substring with start index = 0 is "ab", which is an anagram of "ab".
The substring with start index = 1 is "ba", which is an anagram of "ab".
The substring with start index = 2 is "ab", which is an anagram of "ab".
"""

def findAnagrams(self, s, p):
    """
    :type s: str
    :type p: str
    :rtype: List[int]
    """
    output = []
    pCount = {}
    sCount = {}
    l = 0

    if len(p) > len(q):
        return []

    for i in range(len(p)):
        pCount[p[i]]= 1 + pCount.get(p[i], 0)
        sCount[s[i]] = 1 + sCount.get(s[i], 0)

    if pCount == sCount:
        output.append(l)
    
    for r in range(len(p), len(s)):
        sCount[s[r]] = 1 + sCount.get(s[r],0)
        sCount[s[l]] -= 1
        if sCount[s[l]] == 0:
            sCount.pop(s[l])
        l += 1
        if sCount == pCount:
            output.append(l)
    return output
