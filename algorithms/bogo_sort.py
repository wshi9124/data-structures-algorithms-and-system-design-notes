import random

"""
Bogo Sort- Randomly rearranges value over and over again until they are sorted 
Inefficient because it is random and the number of attempts increase drastically with extra numbers in the array 
Based on luck
Runtime of O(n!) or factorial runtime 
"""

numbers= [20,15,10,200,1]
print(numbers) 

def is_sorted(values):
    for index in range(len(values) - 1):
        if values[index] > values[index + 1]:
            return False 
    return True

def bogo_sort(values):
    attempts = 0
    while not is_sorted(values):
        print(attempts)
        random.shuffle(values)
        attempts += 1
    return(values)

print(bogo_sort(numbers))