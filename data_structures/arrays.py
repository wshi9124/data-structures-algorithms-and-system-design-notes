"""
array- Contiguous data structure with no gaps
In python the values are not stored in memory, instead the array only stores the references 
"""

new_list = [1,2,3]

"""To access value (constant time)"""
result = new_list[0]

"""
Searching for values
Taking the array as is the best that we can do is a linear search (linear time)
If sorted we can do binary search (logarithmic time)
"""
if 1 in new_list:
    print(True) 

for n in new_list:
    if n == 1:
        print(True) 

        break

"""
Inseting values- 3 ways 
1) Insert- inserts and shifts rest of the elements to the right (linear time) 
2) Appending (constant time and constant space)
0,4,8,16,25,35,46... points where python resizes its list when appending new values,
so when you average the space complexity it averages out to constant sapce  
This means that appeniding takes an Ammortized Constant Space Complexity 
3) Extend- add one list to another (makes a series of append calls until all elements are appended to the new list)
Runtime of O(k) where k represents the number of elements in the list that we are adding to our existing list
"""
numbers = [1,2,3]
numbers.insert(1, 20)
print(numbers)

numbers2 = []
numbers2.append(2)
numbers2.append(20)
print("numbers2", numbers2)

numbers3=[] 
numbers3.extend([4, 5, 6])
print("numbers3", numbers3)

"""
Delete- deletes and shift every element to the left
just like insert it has a linear runtime or O(n)
Remove all items: clear()
Remove an item by index and get its value: pop()
Remove an item by value (first instance): remove()
Remove items by index or slice: del
Remove items that meet the condition: List comprehensions
"""

numbers4= [1,2,3,4]
numbers4.clear()
print("numbers4", numbers4)

numbers5= [1,2,3,4]
print("pop of numbers5", numbers5.pop(-1))
print("numbers5", numbers5)

numbers6= [20,1,2,3,4,20]
numbers6.remove(20)
print("numbers6", numbers6)

numbers7= [1,2,3,4]
del numbers7[0:2]
print("numbers7", numbers7)

numbers8= [1,2,3,4,20]
print("Find even in numbers8", [bannanas for bannanas in numbers8 if bannanas%2 == 0])