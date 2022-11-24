"""
Recursive algorithm that continuously splits the array in half until it cannot be further divided. 
If the array has multiple elements, split the array into halves and recursively invoke the merge sort on each of the halves.
When both halves are sorted, the merge operation is applied. 
Merge operation is the process of taking two smaller sorted arrays and combining them to eventually make a larger one.
"""

def merge_sort(list):
    """
    Sorts given list in ascending order
    Returns a new sorted list 

    Steps
    1) Divide: Find midpoint of the list and divide into sublist 
    2) Conquer: Recursively sort the sublists created in previous step
    3) Combine: Merge sorted sublists created in previous step 
    """
    
    """
    First check for naively sorting- if we give merge sort functuon an 
    empty list or a list with one element it is technically already sorted
    """

    if len(list) <= 1:
        return list
    
    left_half, right_half = split(list)
    """
    Recursive postion of the function
    """
    left = merge_sort(left_half)
    right = merge_sort(right_half)

    return merge(left, right)

def split(list):
    """
    Divide the unsorted list at midpoint into sublists 
    Returns two sublists- left and right 
    """
    mid = len(list)//2
    """
    :mid means left of mid point and mid: means right of midpoint
    """
    left = list[:mid]
    right = list[mid:]

    return left, right 

def merge(left, right):
    """
    Merges 2 lists (arrays), sorting them in the process
    Returns a new merged list 
    i variable used for indexes in the left list and j for indexes in the right list 
    """

    l=[]
    i = 0
    j = 0

    while i < len(left) and j < len(right):
        if left[i]  < right[j]:
            l.append(left[i])
            i += 1
        else:
            l.append(right[j])
            j += 1

    """
    Case for when right list is shorter than the left
    """

    while i < len(left):
        l.append(left[i])
        i += 1

    """
    Case for when left list is shorter than right
    """

    while j < len(right):
        l.append(right[j])
        j += 1

    return l

alist = [60, 15, 38, 90, 98, 3, 26, 80, 77]
print(merge_sort(alist))