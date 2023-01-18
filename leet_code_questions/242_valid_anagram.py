"""
Given two strings s and t, return true if t is an anagram of s, and false otherwise.
An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

Example 1:
Input: s = "anagram", t = "nagaram"
Output: true

Example 2:
Input: s = "rat", t = "car"
Output: false
"""

def isAnagram(self, s, t):
    """
    :type s: str
    :type t: str
    :rtype: bool
    """
    hashS = {}
    hashT = {}

    for character in s:
        hashS[character] = 1 + hashS.get(character, 0)
    for character in t:
        hashT[character] = 1 + hashT.get(character,0)

    if hashS == hashT:
        return True
    return False