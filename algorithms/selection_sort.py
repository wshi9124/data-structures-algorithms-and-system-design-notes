"""
Selection sort- sorts an array by repeatedly finding the minimum element 
from the unsorted array and putting it at the beginning or a new array. 

Very slow but better than bogo sort because each pass through the list 
brings it a little closer to completion

This example will use 2 arrays (unsorted and sorted) to keep code simplier 
However, it is better to only use one array  

Selection sort has a time complexity of O(n2) or qaudratic runtime (not very efficient)
"""

def selection_sort(values):
    sorted_list= []
    for i in range(0, len(values)):
        index_to_move = index_of_min(values)
        # adding value to sorted_list by poping it off the unsorted list 
        sorted_list.append(values.pop(index_to_move))
        # This is to just display process in console
        print("sorted list", sorted_list)
    return sorted_list

def index_of_min(values):
    min_index = 0
    for i in range(1, len(values)):
        # checking if value is less than the value of the first index 
        if values[i] < values[min_index]:
            # if it is we set that as the new min_index
            min_index = i  
    return min_index
             
numbers= [50,100,20,10,200,5]
print("Final Result", selection_sort(numbers)) 