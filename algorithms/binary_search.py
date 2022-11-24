def binary_search(list, target):
    first = 0
    last= len(list) - 1 
    """length of list -1 is always used to get last index of list"""
    
    """// is floor division operator it rounds down to the nearest whole number"""
    """while loop is what causes runtime to grow from constant time to log"""
    while first <= last:
        midpoint= (first + last) //2

        if list[midpoint] == target:
            return midpoint
        elif list[midpoint] < target:
            first= midpoint + 1 
        else:
            last = midpoint -1  
    
    return None

def verify(index):
    if index is not None:
        print("Target found at index: ", index)
    else:
        print("Target not found in list")

numbers = [1,2,3,4,5,6,7,8,9,10]

result= binary_search(numbers, 12)
verify(result)

result= binary_search(numbers, 6)
verify(result)

"""
List has to be sorted
Logarithmic runtime O(log n) or O(ln n) 
Iterative solution- generally means that the solution is implemented using a loop structure
Space complexity of the iterative binary search is constant O(1)
"""





    