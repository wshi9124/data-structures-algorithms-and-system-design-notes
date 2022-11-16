def recursive_binary_search(list, target):
    if len(list) == 0:
        return False
    else:
        midpoint = (len(list)) // 2

        if list[midpoint] == target:
            return True
        else:
            if list[midpoint] < target:
                return recursive_binary_search(list[midpoint + 1:], target) 
            else:
                return recursive_binary_search(list[:midpoint], target)

def verify(result):
    print("Target found: ", result)

numbers= [1,2,3,4,5,6,7,8]

result= recursive_binary_search(numbers, 12)
verify(result)

result= recursive_binary_search(numbers, 6)
verify(result)

"""
Recursive function: function that calls on itself
In function above, it is:
return recursive_binary_search(list[midpoint + 1:], target) 
return recursive_binary_search(list[:midpoint], target)

Recursive functions always need a stopping condition or base case 
In the function above, there is 2:
if len(list) == 0:
    return False

if list[midpoint] == target:
    return True

The number of times a recursive function calls on itself is callled recursive depth
Python prefers an iterative solution over a recursive solution
One reason is becasue python doesnt recall tail call optamization
Space complexity of the recursive version of binary search is logarithmic O(log n) of becasue it keeps creating new lists for python
""" 