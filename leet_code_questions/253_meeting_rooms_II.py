"""
Given an array of meeting time intervals intervals where intervals[i] = [starti, endi], return the minimum number of conference rooms required.

Example 1:
Input: intervals = [[0,30],[5,10],[15,20]]
Output: 2

Example 2:
Input: intervals = [[7,10],[2,4]]
Output: 1
 
Constraints:
1 <= intervals.length <= 104
0 <= starti < endi <= 106
"""

def minMeetingRooms(self, intervals: List[List[int]]) -> int:   
    """
    nlogn time complexity 
    """
    start = []

    for i in range(len(intervals)):
        start.append(intervals[i][0])
    
    start.sort()

    end = []

    for i in range(len(intervals)):
        end.append(intervals[i][1])
    
    end.sort()

    result, count = 0,0
    s, e = 0,0

    while s < len(intervals):
        if start[s] < end[e]:
            count += 1
            s += 1
        else:
            count -= 1
            e += 1
        result = max(result, count)
    return result
    