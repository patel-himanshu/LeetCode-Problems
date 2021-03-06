# Question: https://leetcode.com/explore/challenge/card/october-leetcoding-challenge/559/week-1-october-1st-october-7th/3481/

"""
Given an array of distinct integers candidates and a target integer target, return a list of all unique combinations of 
candidates where the chosen numbers sum to target. You may return the combinations in any order.
The same number may be chosen from candidates an unlimited number of times.
Two combinations are unique if the frequency of at least one of the chosen numbers is different.

Example 1:
    Input: candidates = [2,3,6,7], target = 7
    Output: [[2,2,3],[7]]
    Explanation:
        2 and 3 are candidates, and 2 + 2 + 3 = 7. Note that 2 can be used multiple times.
        7 is a candidate, and 7 = 7.
        These are the only two combinations.

Example 2:
    Input: candidates = [2,3,5], target = 8
    Output: [[2,2,2,2],[2,3,3],[3,5]]

Example 3:
    Input: candidates = [2], target = 1
    Output: []

Example 4:
    Input: candidates = [1], target = 1
    Output: [[1]]

Example 5:
    Input: candidates = [1], target = 2
    Output: [[1,1]]
 
Constraints:
    (1) 1 <= candidates.length <= 30
    (2) 1 <= candidates[i] <= 200
    (3) All elements of candidates are distinct.
    (4) 1 <= target <= 500
"""

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        if not candidates:
            return []
        
        ans = []
        candidates.sort()
        
        def helper(idx, target, path):
            if target < 0:
                return
            if target == 0:
                ans.append(path)
                return
            
            for i in range(idx, len(candidates)):
                if candidates[i] > target:
                    break
                helper(i, target - candidates[i], path + [candidates[i]])
                
        helper(0, target, [])
        return ans