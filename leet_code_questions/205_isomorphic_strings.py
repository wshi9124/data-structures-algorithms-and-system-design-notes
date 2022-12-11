"""
Given two strings s and t, determine if they are isomorphic.
Two strings s and t are isomorphic if the characters in s can be replaced to get t.
All occurrences of a character must be replaced with another character while preserving the order of characters. 
No two characters may map to the same character, but a character may map to itself.

Example 1:

Input: s = "egg", t = "add"
Output: true
Example 2:

Input: s = "foo", t = "bar"
Output: false
Example 3:

Input: s = "paper", t = "title"
Output: true
"""

def isIsomorphic(s, t):
    """
    :type s: str
    :type t: str
    :rtype: bool
    Most efficient way is to use a hashmap 
    Time complexity: O(n)
    Space complexity: O(1)
    """
    map_through_s_t = {}
    map_through_t_s = {}

    for i in range(len(s)):
        c1 = s[i]
        c2 = t[i]
        if (c1 in map_through_s_t and map_through_s_t[c1] != c2) or (c2 in map_through_t_s and map_through_t_s[c2] != c1):
            return False
        map_through_s_t[c1] = c2
        map_through_t_s[c2] = c1

    return True

s = "egg"
t= "add"
print(isIsomorphic(s,t))
s= "foo"
t= "bar"
print(isIsomorphic(s,t))