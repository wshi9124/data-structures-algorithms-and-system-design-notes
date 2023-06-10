"""
You are given a network of n nodes, labeled from 1 to n. You are also given times, a list of travel times as directed edges times[i] = (ui, vi, wi), where ui is the source node, vi is the target node, and wi is the time it takes for a signal to travel from source to target.
We will send a signal from a given node k. Return the minimum time it takes for all the n nodes to receive the signal. If it is impossible for all the n nodes to receive the signal, return -1.

Example 1:
Input: times = [[2,1,1],[2,3,1],[3,4,1]], n = 4, k = 2
Output: 2

Example 2:
Input: times = [[1,2,1]], n = 2, k = 1
Output: 1

Example 3:
Input: times = [[1,2,1]], n = 2, k = 2
Output: -1
"""

def networkDelayTime(self, times, n, k):
    #dijkstra's algorithm
    # used for finding the shortest distance from starting node to target node in a weighted graph 
    # O(E * logV)
    #BFS and minHeap
    
    edges = {i:[] for i in range(1,n+1)}

    for u,v,w in times:
        edges[u].append((v,w))
    
    time = 0
    minHeap = [(0,k)]
    visit = set()

    while minHeap:
        w1, n1 = heapq.heappop(minHeap)
        if n1 in visit:
            continue
        visit.add(n1)
        time = w1
        for n2, w2 in edges[n1]:
            heapq.heappush(minHeap, (w1+w2, n2))
    return time if len(visit) == n else -1