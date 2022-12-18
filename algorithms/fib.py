"""
Write a function that takes in a number as an arguement 
The function should return the n-th number of the Fibonacci sequence 

The first and second number of the sequence is 1 
To generate the next number of the sequence, we sum the previous two numbers 
"""

def fib(input):
    """
    Works, but very slow
    Time complexity: O(2^n)
    Space Complexity; O(n)
    """
    if input <= 2: return 1
    return fib(input-1) + fib(input-2)
    
def fib_using_memoization(input):
    """
    Memoization- hash map, keys will be arguement to our function, value will be return value  
    Time complexity: O(n)
    Space Complexity: O(n)
    """
    memo = {}

    if input <= 2: 
        return 1

    if input in memo:
        return memo[input]
    else:
        result = fib_using_memoization(input-1) + fib_using_memoization(input-2)
        memo[input] = result
        return result

def fib_more_efficient(n):
    memo= {0:0, 1:1}

    # n+1 is so number doesnt go out of range
    for i in range(2, n+1):
        print(i)
        memo[i] = memo[i-1] + memo[i-2]
        
    return memo[n]

fib_more_efficient(4)