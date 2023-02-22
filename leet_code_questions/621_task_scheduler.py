"""
Given a characters array tasks, representing the tasks a CPU needs to do, where each letter represents a different task. Tasks could be done in any order. Each task is done in one unit of time. For each unit of time, the CPU could complete either one task or just be idle.
However, there is a non-negative integer n that represents the cooldown period between two same tasks (the same letter in the array), that is that there must be at least n units of time between any two same tasks.
Return the least number of units of times that the CPU will take to finish all the given tasks.

Example 1:
Input: tasks = ["A","A","A","B","B","B"], n = 2
Output: 8
Explanation: 
A -> B -> idle -> A -> B -> idle -> A -> B
There is at least 2 units of time between any two same tasks.

Example 2:
Input: tasks = ["A","A","A","B","B","B"], n = 0
Output: 6
Explanation: On this case any permutation of size 6 would work since n = 0.
["A","A","A","B","B","B"]
["A","B","A","B","A","B"]
["B","B","B","A","A","A"]
...
And so on.

Example 3:
Input: tasks = ["A","A","A","A","A","A","B","C","D","E","F","G"], n = 2
Output: 16
Explanation: 
One possible solution is
A -> B -> C -> A -> D -> E -> A -> F -> G -> A -> idle -> idle -> A -> idle -> idle -> A
"""

def leastInterval(self, tasks, n):
    """
    :type tasks: List[str]
    :type n: int
    :rtype: int
    O(n * m)
    m idle time
    """

    hash = {}

    for t in tasks:
        hash[t] = 1 + hash.get(hash, 0)
    
    maxHeap = []

    for count in hash.values():
        maxHeap.append(-count)

    heapq.heapify(maxHeap)
    q = collections.deque()
    time = 0

    while maxHeap or q:
        time += 1
        if maxHeap:
            count = heapq.heappop(maxHeap) + 1
            if count != 0:
                q.append([count, time + n])
        if q and q[0][1] == time:
            heapq.heappush(maxHeap, q.popleft()[0])

    return time