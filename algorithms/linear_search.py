"""Linear Search has a linear runtime or O(n)"""

def linear_search(list, target):
    """ 
    returns the index position of the target if found, else returns None 
    len(list) constant time operation n(1)
    """
    for i in range(0, len(list)):
        if list[i] == target:
            return i
    return None 

def verify(index):
    if index is not None:
        print("Target found at index: ", index)
    else:
        print("Target not found in list")

numbers = [1,2,3,4,5,6,7,8,9,10]

result= linear_search(numbers, 12)
verify(result)

result= linear_search(numbers, 6)
verify(result)

"""
Another example of linear search
"""

def index_of_item(collection, target):
    for i in range(0, len(collection)):
        if collection[i] == target:
            return i 
    return None 

names = ["Willie","Alan","Kai","Tony"]

n = "Alan"
print(index_of_item(names,n))