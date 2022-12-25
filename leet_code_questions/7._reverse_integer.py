"""
Given a signed 32-bit integer x, return x with its digits reversed. 
If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.
Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

Example 1:
Input: x = 123
Output: 321

Example 2:
Input: x = -123
Output: -321

Example 3:
Input: x = 120
Output: 21
"""

def reverse(x):
    """
    :type x: int
    :rtype: int
    -2^31 = 2147483648 ends with 8
    2^31 - 1 = -2147483647 ends with 7
    """
    max_value = 2147483648
    min_value = -2147483647
    result = 0 
    positive_or_negative = 1

    if x < 0:
        positive_or_negative = -1
        x = x * positive_or_negative
    while x:
        remainder = x % 10 
        result = result * 10 + remainder
        x = x // 10
    if result > max_value or result < min_value:
        return 0
    return result * positive_or_negative

print(reverse(-123))