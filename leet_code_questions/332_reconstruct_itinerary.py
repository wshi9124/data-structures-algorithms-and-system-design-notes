"""
You are given a list of airline tickets where tickets[i] = [fromi, toi] represent the departure and the arrival airports of one flight. Reconstruct the itinerary in order and return it.
All of the tickets belong to a man who departs from "JFK", thus, the itinerary must begin with "JFK". If there are multiple valid itineraries, you should return the itinerary that has the smallest lexical order when read as a single string.

For example, the itinerary ["JFK", "LGA"] has a smaller lexical order than ["JFK", "LGB"].
You may assume all tickets form at least one valid itinerary. You must use all the tickets once and only once.

Example 1:
Input: tickets = [["MUC","LHR"],["JFK","MUC"],["SFO","SJC"],["LHR","SFO"]]
Output: ["JFK","MUC","LHR","SFO","SJC"]

Example 2:
Input: tickets = [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
Output: ["JFK","ATL","JFK","SFO","ATL","SFO"]
Explanation: Another possible reconstruction is ["JFK","SFO","ATL","JFK","ATL","SFO"] but it is larger in lexical order.
"""
def findItinerary(self, tickets):
    # len(result) is always going to be len(tickets) + 1
    adj = {src:[] for src, des in tickets}

    tickets.sort()

    for src, des in tickets:
        adj[src].append(des)
    
    result = ["JFK"]
    def dfs(src):
        if len(result) == len(tickets) + 1:
            return True
        if src not in adj:
            return False
        
        # temp = list(adj[src])
        # we don't want to update a list while we iterate through it, so, we make a copy first
        for i, v in enumerate(adj[src]):
            adj[src].pop(i)
            result.append(v)

            if dfs(v): return True
            # now we backtrack 
            adj[src].insert(i,v)
            result.pop()
        
        return False
    dfs("JFK")
    return result



