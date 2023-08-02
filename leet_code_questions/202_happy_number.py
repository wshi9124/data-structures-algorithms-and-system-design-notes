"""
Write an algorithm to determine if a number n is happy.
A happy number is a number defined by the following process:
Starting with any positive integer, replace the number by the sum of the squares of its digits.
Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
Those numbers for which this process ends in 1 are happy.
Return true if n is a happy number, and false if not.

Example 1:
Input: n = 19
Output: true
Explanation:
12 + 92 = 82
82 + 22 = 68
62 + 82 = 100
12 + 02 + 02 = 1

Example 2:
Input: n = 2
Output: false
"""

def isHappy(self, n):
    # # O(n) memory
    visit = set()   

    while n not in visit:
        visit.add(n)
        n = self.sumOfSquares(n)

        if n == 1:
            return True
    return False

    #more efficient way
    slow, fast = n, self.sumOfSquares(n)

    while slow != fast:
        slow = self.sumOfSquares(slow)
        fast = self.sumOfSquares(fast)
        fast = self.sumOfSquares(fast)
    
    return True if slow == 1 else False

def sumOfSquares(self, n):
    output = 0

    while n:
        digit = n % 10
        digit = digit ** 2
        output += digit 
        n = n // 10
    
    return output