"""
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

Example 1:
Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]

Example 2:
Input: n = 1
Output: ["()"]
"""
def generateParenthesis(self, n):
    """
    n pairs
    2^n number of parenthesis - powerset
    :type n: int
    :rtype: List[str]
    backtracking
    only add opening parenthesis if open < n 
    only add closing parenthesis if closing < open
    only valid if open == close == n
    """

    stack = []
    result = []

    def backTrack(openN, closeN):
        if openN == closeN == n:
            result.append("".join(stack))
        
        if openN < n:
            stack.append("(")
            backTrack(openN + 1, closeN)
            stack.pop()
        if closeN < openN:
            stack.append(")")
            backTrack(openN + closeN + 1)
            stack.pop()
    
    backTrack(0,0)
    return result