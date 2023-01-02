"""
You are a traveler on a 2d grid. You begin in the top-left corner and your goal is to travel to the bottom-right corner. 
You can only move down or right.  

ex: grid_traveler(3) 
"""
def grid_traveler(m,n):
    # in a one by one grid there is only one way to travel from start to end 
    if (m == 1 and n == 1): return 1
    # if m or n is zero, there is no way to travel from start to end   
    if (m == 0 or n == 0): return 0 
    return grid_traveler(m-1, n) + grid_traveler(m, n-1)

print(grid_traveler(1,1)) 
print(grid_traveler(2,3)) 