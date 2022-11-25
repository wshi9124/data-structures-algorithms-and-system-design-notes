"""
Recursive algorithm that continuously splits the array in half until it cannot be further divided. 
If the array has multiple elements, split the array into halves and recursively invoke the merge sort on each of the halves.
When both halves are sorted, the merge operation is applied. 
Merge operation is the process of taking two smaller sorted arrays and combining them to eventually make a larger one.

Overall merge sort takes O(n log n) or quasilinear time or log linear time 
It takes O(n) or linear space becasue the previously split lists are deleted from memory 
so only last merge matters which depends on size of list or n 
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

    Split takes overall O(log n), logrithmic time because split time depends on the number of items in the array 
    """
    mid = len(list)//2
    """
    :mid means left of mid point and mid: means right of midpoint
    technically the runtime is O(k log n) becasue we used a slicing operation 
    we can fix this problem by using a iterative approach without using list slicing 
    """
    left = list[:mid]
    right = list[mid:]

    return left, right 

def merge(left, right):
    """
    Merges 2 lists (arrays), sorting them in the process
    Returns a new merged list 
    i variable used for indexes in the left list and j for indexes in the right list 

    Merge runs in overall O(n) or linear time    
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

def verify_sorted(list):
    """
    Recursive way to check if list is sorted instead of the iterative way by using a while loop
    """
    n = len(list)

    if n == 0 or n == 1:
        return True
    
    return list[0] < list[1] and verify_sorted(list[1:])

alist = [60, 15, 38, 90, 98, 3, 26, 80, 77]
s= merge_sort(alist)
print(s)
print("is alist sorted?", verify_sorted(alist))
print("is s sorted?", verify_sorted(s))