"""
Given an array of integers temperatures represents the daily temperatures, return an array answer such that answer[i] is the number of days you have to wait after the ith day to get a warmer temperature. If there is no future day for which this is possible, keep answer[i] == 0 instead.

Example 1:
Input: temperatures = [73,74,75,71,69,72,76,73]
Output: [1,1,4,2,1,1,0,0]

Example 2:
Input: temperatures = [30,40,50,60]
Output: [1,1,1,0]

Example 3:
Input: temperatures = [30,60,90]
Output: [1,1,0]
"""

def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
    # result = [0] * len(temperatures)
    # stack = [] #[[temperature, index]]

    # for i, t in enumerate(temperatures):
    #     while stack and t > stack[-1][0]:
    #         stackTemp, stackInd = stack.pop()
    #         result[stackInd] = (i - stackInd)
    #     stack.append([t,i])
    # return result

    result = [0] * len(temperatures)

    stack = []

    for i, t in enumerate(temperatures):
        while stack and t > stack[-1][0]:
            temperature, index = stack.pop() 
            result[index] = i - index
        stack.append([t, i])
    return result