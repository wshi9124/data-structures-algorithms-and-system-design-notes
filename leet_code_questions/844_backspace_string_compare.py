"""
Given two strings s and t, return true if they are equal when both are typed into empty text editors. '#' means a backspace character.

Note that after backspacing an empty text, the text will continue empty.


Example 1:
Input: s = "ab#c", t = "ad#c"
Output: true
Explanation: Both s and t become "ac".

Example 2:
Input: s = "ab##", t = "c#d#"
Output: true
Explanation: Both s and t become "".

Example 3:
Input: s = "a#c", t = "b"
Output: false
Explanation: s becomes "c" while t becomes "b".
"""

def backspaceCompare(self, s, t):
    """
    :type s: str
    :type t: str
    :rtype: bool
    """
    stackS = []
    stackT= []
    
    for letters in s:
        if letters >= "a" and letters <= "z":
            stackS.append(letters)
        elif stackS and letters == "#":
            stackS.pop()
    for letters in t:
        if letters >= "a" and letters <= "z":
            stackT.append(letters)
        elif stackT and letters == "#":
            stackT.pop()
    if stackS == stackT:
        return True
    return False