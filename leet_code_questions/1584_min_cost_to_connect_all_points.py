"""
You are given an array points representing integer coordinates of some points on a 2D-plane, where points[i] = [xi, yi].
The cost of connecting two points [xi, yi] and [xj, yj] is the manhattan distance between them: |xi - xj| + |yi - yj|, where |val| denotes the absolute value of val.
Return the minimum cost to make all points connected. All points are connected if there is exactly one simple path between any two points.

Example 1:
Input: points = [[0,0],[2,2],[3,10],[5,2],[7,0]]
Output: 20

Explanation: 
We can connect the points as shown above to get the minimum cost of 20.
Notice that there is a unique path between every pair of points.

Example 2:
Input: points = [[3,12],[-2,5],[-4,1]]
Output: 18
"""

def minCostConnectPoints(self, points):
    # minimum spanning tree- prims algorithm 
    # O(n**2logn) minHeap
    # we want to connect every point together without forming a cycle (n-1) edges

    n = len(points)

    adj = {i:[] for i in range(n)} # i : list of [cost, node]

    for i in range(n):
        x1, y1 = points[i]
        for j in range(i+1, n):
            x2, y2 = points[j]
            distance = abs(x1-x2) + abs(y1-y2)
            adj[i].append([distance, j])
            adj[j].append([distance, i])
    
    #prims algorithm
    result = 0
    visit = set()
    minHeap = [[0,0]] #[cost,point]

    while len(visit) < n:
        cost, i  = heapq.heappop(minHeap)
        if i in visit:
            continue
        result += cost
        visit.add(i)
        for neiCost, nei in adj[i]:
            if nei not in visit:
                heapq.heappush(minHeap, [neiCost, nei])
    return result



