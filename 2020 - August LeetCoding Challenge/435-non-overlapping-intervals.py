# Question: https://leetcode.com/explore/featured/card/august-leetcoding-challenge/551/week-3-august-15th-august-21st/3425/

"""
Given a collection of intervals, find the minimum number of intervals you need to remove to make the rest of the intervals non-overlapping.

Example 1:
    Input: [[1,2],[2,3],[3,4],[1,3]]
    Output: 1
    Explanation: [1,3] can be removed and the rest of intervals are non-overlapping.

Example 2:
    Input: [[1,2],[1,2],[1,2]]
    Output: 2
    Explanation: You need to remove two [1,2] to make the rest of intervals non-overlapping.

Example 3:
    Input: [[1,2],[2,3]]
    Output: 0
    Explanation: You don't need to remove any of the intervals since they're already non-overlapping.

Note:
    (1) You may assume the interval's end point is always bigger than its start point.
    (2) Intervals like [1,2] and [2,3] have borders "touching" but they don't overlap each other.
"""

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if not intervals: return 0
        
        intervals.sort(key = lambda x: x[1])
        ans = 0
        i = 1
        
        while i < len(intervals):
            if intervals[i][0] < intervals[i-1][1]:
                intervals.pop(i)
                ans += 1
            else:
                i += 1
            
        return ans