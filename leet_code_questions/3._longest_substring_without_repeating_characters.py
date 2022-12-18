"""
Given a string s, find the length of the longest substring without repeating characters.

Example 1:
Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.

Example 2:
Input: s = "bbbbb"
Output: 1 
Explanation: The answer is "b", with the length of 1.

Example 3:
Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
"""

def lengthOfLongestSubstring(self, s):
    """
    :type s: str
    :rtype: int
    Time ccomplexity O(n)
    Space ccomplexity O(n)
    We use 2 ppinters to solve the question
    """
    new_set = set()
    left = 0 
    result = 0

    for right in range(len(s)):
        while s[right] in new_set:
            new_set.remove(s[left])
            left += 1
        new_set.add(s[right])
        result = max(result, right - left + 1)
    return result
    
    
