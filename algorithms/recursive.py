"""
Recursive funtion needs a case to call on itself 
Also needs a base case for the recursion to stop
"""
def sum(numbers):
    total = 0
    for number in numbers:
        total += number
    return total

def recursive_sum(numbers):
    """
    Python treats a list with values as True and a list with no values as False
    The if statement keeps it from becoming an infinite loop 
    If there are no numbers on the list return sum of 0 
    """
    if not numbers:
        return 0
    remaining_sum = recursive_sum(numbers[1:])
    return numbers[0] + remaining_sum



numbers = [20,49,86,200,50]
print(sum(numbers))
print(recursive_sum(numbers))