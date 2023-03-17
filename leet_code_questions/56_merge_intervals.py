"""
Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.

Example 1:
Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].

Example 2:
Input: intervals = [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.
"""

def merge(self, intervals: List[List[int]]) -> List[List[int]]:
    intervals.sort(key = lambda pair:pair[0])
    output = [intervals[0]]

    for start, end in intervals:
        lastEnd = output[-1][1]
        if start <= lastEnd:
            output[-1][1] = max(lastEnd, end)
        else:
            output.append([start, end])
    return output

    # for i in range(len(intervals)):
    #     if intervals[i][0] <= output[-1][1]:
    #         output[-1][1] = max(output[-1][1], intervals[i][1])
    #     else:
    #         output.append([intervals[i][0], intervals[i][1]])
    # return output