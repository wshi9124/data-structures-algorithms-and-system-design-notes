"""
Given a string s which consists of lowercase or uppercase letters, return the length of the longest palindrome that can be built with those letters.
Letters are case sensitive, for example, "Aa" is not considered a palindrome here.

Example 1:
Input: s = "abccccdd"
Output: 7
Explanation: One longest palindrome that can be built is "dccaccd", whose length is 7.

Example 2:
Input: s = "a"
Output: 1
Explanation: The longest palindrome that can be built is "a", whose length is 1.

"""
def longestPalindrome(s):
    """
    :type s: str
    :rtype: int
    """
    letters = {}

    for char in s:
        if char not in letters:
            letters[char] = 1
        else:
            letters[char] = letters[char] + 1
    
    result = 0
    odd = 0

    for i in letters.values():
        if i > 1:
            if i % 2 == 0:
                result += i
            else:
                result += (i-1)
                odd += 1
        else:
            odd += 1

    if odd > 0:
        result += 1
    
    return result 
