"""
You are given an m x n grid rooms initialized with these three possible values.
-1 A wall or an obstacle.
0 A gate.
INF Infinity means an empty room. We use the value 231 - 1 = 2147483647 to represent INF as you may assume that the distance to a gate is less than 2147483647.
Fill each empty room with the distance to its nearest gate. If it is impossible to reach a gate, it should be filled with INF.

Example 1:
Input: rooms = [[2147483647,-1,0,2147483647],[2147483647,2147483647,2147483647,-1],[2147483647,-1,2147483647,-1],[0,-1,2147483647,2147483647]]
Output: [[3,-1,0,1],[2,2,1,-1],[1,-1,2,-1],[0,-1,3,4]]

Example 2:
Input: rooms = [[-1]]
Output: [[-1]]
"""

def wallsAndGates(self, rooms):
    rows, cols = len(rooms), len(rooms[0])
    visit = set()
    q = collections.deque()

    def addRoom(r,c):
        if r < 0 or c < 0 or r >= rows or c >= cols or (r,c) in visit or rooms[r][c] == -1:
            return
        visit.add((r,c))
        q.append((r,c))

    for r in range(rows):
        for c in range(cols):
            if rooms[r][c] == 0:
                q.append((r,c))
                visit.add((r,c))
    
    distance = 0
    while q:
        for i in range(len(q)):
            r, c = q.popleft()
            rooms[r][c] = distance
            addRoom(r + 1, c)
            addRoom(r - 1, c)
            addRoom(r, c + 1)
            addRoom(r, c - 1)
        distance += 1
