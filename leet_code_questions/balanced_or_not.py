"""
Consider a string of the characters < and > only.
The string is balanced if each < always appears before a corresponding > character 

To balance a string, any > character can be replaced with <>. Given an expression and a maximum 
number of replacements, determine whether the string can be blanced.

Example:
expression = ["<<>>", "<>", "<><>", ">>", "><><"]
maxReplacements = [0, 1, 2, 2, 2, 2]

Process a series of expressions and their corresponding maxReplacements.
(First 3 expressions are already balanced, expressions[3] can be balanced, neither of the last 2 strings can be balanced)

Return an array of intergers where element[i] contains a 1 if expressions[i] is balanced or a 0 if it is 
"""

def balancedOrNot(self, expressions, maxReplacements):
    result = []

    for i in range(0, len(expressions)):
        currentExpressions = expressions[i]
        replacementLeft = maxReplacements[i]

        stack = []

        for c in currentExpressions:
            if c == "<":
                stack.append(c)
            else: # if char == ">"
                if len(stack) == 0:
                    replacementLeft -= 1
                else:
                    stack.pop()
                if replacementLeft < 0:
                    break
        result.append(1 if replacementLeft >= 1 and len(stack) == 0 else 0)
    return result


