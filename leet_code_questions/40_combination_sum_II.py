"""
Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sum to target.
Each number in candidates may only be used once in the combination.
Note: The solution set must not contain duplicate combinations.

Example 1:=
Input: candidates = [10,1,2,7,6,1,5], target = 8
Output: 
[
[1,1,6],
[1,2,5],
[1,7],
[2,6]
]

Example 2:
Input: candidates = [2,5,2,1,2], target = 5
Output: 
[
[1,2,2],
[5]
]
"""
def combinationSum2(self, candidates, target):
    candidates.sort()
    result = []

    def backTrack(curr, position, target):
        if target == 0:
            result.append(curr.copy())
        if target < 0:
            return
        
        prev = -1
        for i in range(position, len(candidates)):
            if candidates[i] == prev:
                continue
            curr.append(candidates[i])
            backTrack(curr, i + 1, target - candidates[i])
            curr.pop()

            prev = candidates[i]
        
    backTrack([], 0, target)
    return result

        