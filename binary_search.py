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