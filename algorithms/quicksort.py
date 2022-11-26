"""
Quicksort- a divide and conquer algorithm just like merge sort
1) We first pick a pivot point (for example below its the last value)
2) Then we append all the numbers higher and lower than the pivot point 
and use a recursive function to call itself again until everything is sorted

Best case runtime of O(n log n) or quasilinear or log linear
Worst case is O(n^2) 
However, most times it performs closer to the best case by picking a pivot at random  

Quicksort is more used in the real world than merge sort 
"""

def quicksort(values):
    if len(values) <= 1:
        return values
    less_than_pivot = []
    greater_than_pivot = []
    # pivot point can be any value 
    pivot = values[-1]
    for value in values[:-1]:
        if value <= pivot:
            less_than_pivot.append(value)
        else:
            greater_than_pivot.append(value)
    return quicksort(less_than_pivot) + [pivot] + quicksort(greater_than_pivot)

numbers= [10,5,30,45,90,2]
print("Quicksort", quicksort(numbers))
