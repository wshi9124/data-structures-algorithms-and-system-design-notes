"""
Write a function that takes the binary representation of an unsigned integer and returns the number of '1' bits it has (also known as the Hamming weight).

Note:
Note that in some languages, such as Java, there is no unsigned integer type. In this case, the input will be given as a signed integer type. It should not affect your implementation, as the integer's internal binary representation is the same, whether it is signed or unsigned.
In Java, the compiler represents the signed integers using 2's complement notation. Therefore, in Example 3, the input represents the signed integer. -3.
 
Example 1:
Input: n = 00000000000000000000000000001011
Output: 3
Explanation: The input binary string 00000000000000000000000000001011 has a total of three '1' bits.

Example 2:
Input: n = 00000000000000000000000010000000
Output: 1
Explanation: The input binary string 00000000000000000000000010000000 has a total of one '1' bit.

Example 3:
Input: n = 11111111111111111111111111111101
Output: 31
Explanation: The input binary string 11111111111111111111111111111101 has a total of thirty one '1' bits.
"""

def hammingWeight(self, n: int) -> int:
    #time complexity is O(32) because n is guarentee to be 32 bit integer
    result = 0

    while n > 0:
        result += n % 2
        # bit shift to the right by one
        n = n >> 1
    return result

    # optimized solution
    # instead of looking at all the bits we only look at the bits that are 1
    # O(1) time complexity
    #  n = n & (n -1) works because
    # ex: n = 10000001  n - 1 = 10000000    n & (n - 1) = 10000000
    # -> n - 1 = 01111111 
    # we got rid of the rightmost 1 bit so that the other ones don't matter 
    
    result = 0

    while n > 0:
        result += 1
        n = n & (n - 1)

    return result 
    