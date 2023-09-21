"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:
Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
 

Example 1:
Input: s = "()"
Output: true

Example 2:
Input: s = "()[]{}"
Output: true

Example 3:
Input: s = "(]"
Output: false
"""
def isValid(s):
    """
    :type s: str
    :rtype: bool
    """

    # stack = []
    # hashP = {')':'(', '}':'{', ']':'['}

    # for character in s:
    #     if character in hashP:
    #         if stack and stack[-1] == hashP[character]:
    #             stack.pop()
    #         else:
    #             return False
    #     else:
    #         stack.append(character)

    # if not stack:
    #     return True
    # else: 
    #     return False

    stack = []
    hashmap = {"}":"{", "]":"[", ")":"("}

    for c in s:
        if c not in hashmap:
            stack.append(c)
            continue
        if not stack or stack[-1] != hashmap[c]:
            return False
        stack.pop()
    return not stack  