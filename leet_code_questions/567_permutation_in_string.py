"""
Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.
In other words, return true if one of s1's permutations is the substring of s2.

Example 1:
Input: s1 = "ab", s2 = "eidbaooo"
Output: true
Explanation: s2 contains one permutation of s1 ("ba").
Example 2:

Input: s1 = "ab", s2 = "eidboaoo"
Output: false
"""

def checkInclusion(self, s1, s2):
    if len(s1) > len(s2):
            return False
        
    s1Count = {"a":0, "b":0, "c":0, "d":0, "e":0, "f":0, "g":0, "h":0, "i":0, "j":0, "k":0, 
    "l":0, "m":0, "n":0, "o":0, "p":0, "q":0, "r":0, "s":0, "t":0, "u":0, "v":0, "w":0, "x":0, "y":0, "z":0}

    s2Count = {"a":0, "b":0, "c":0, "d":0, "e":0, "f":0, "g":0, "h":0, "i":0, "j":0, "k":0, 
    "l":0, "m":0, "n":0, "o":0, "p":0, "q":0, "r":0, "s":0, "t":0, "u":0, "v":0, "w":0, "x":0, "y":0, "z":0}

    for i in range(len(s1)):
        s1Count[s1[i]] += 1
        s2Count[s2[i]] += 1
    
    if s1Count == s2Count:
        return True
    
    l = 0
    r = len(s1) -1

    while r < len(s2) -1:
        s2Count[s2[l]] -= 1
        l += 1
        r += 1
        s2Count[s2[r]] += 1
        if s1Count == s2Count:
            return True
    return False
