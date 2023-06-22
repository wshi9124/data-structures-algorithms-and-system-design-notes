"""
You are given a string s. We want to partition the string into as many parts as possible so that each letter appears in at most one part.
Note that the partition is done so that after concatenating all the parts in order, the resultant string should be s.
Return a list of integers representing the size of these parts.

Example 1:
Input: s = "ababcbacadefegdehijhklij"
Output: [9,7,8]
Explanation:
The partition is "ababcbaca", "defegde", "hijhklij".
This is a partition so that each letter appears in at most one part.
A partition like "ababcbacadefegde", "hijhklij" is incorrect, because it splits s into less parts.

Example 2:
Input: s = "eccbbbbdec"
Output: [10]
"""

def partitionLabels(self, s):
    count = {}
    res = []
    i, length = 0, len(S)
    for j in range(length):
        c = S[j]
        count[c] = j

    curLen = 0
    goal = 0
    while i < length:
        c = S[i]
        goal = max(goal, count[c])
        curLen += 1

        if goal == i:
            res.append(curLen)
            curLen = 0
        i += 1
    return res