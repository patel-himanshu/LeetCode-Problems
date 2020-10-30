# Question: https://leetcode.com/explore/challenge/card/october-leetcoding-challenge/563/week-5-october-29th-october-31st/3512/

"""
You are given an array representing a row of seats where seats[i] = 1 represents a person sitting in the ith seat, and 
seats[i] = 0 represents that the ith seat is empty (0-indexed). There is at least one empty seat, and at least one person sitting.
Alex wants to sit in the seat such that the distance between him and the closest person to him is maximized. 
Return that maximum distance to the closest person.
 
Example 1:
    Input: seats = [1,0,0,0,1,0,1]
    Output: 2
    Explanation: 
        If Alex sits in the second open seat (i.e. seats[2]), then the closest person has distance 2.
        If Alex sits in any other open seat, the closest person has distance 1.
        Thus, the maximum distance to the closest person is 2.

Example 2:
    Input: seats = [1,0,0,0]
    Output: 3
    Explanation: 
        If Alex sits in the last seat (i.e. seats[3]), the closest person is 3 seats away.
        This is the maximum distance possible, so the answer is 3.

Example 3:
    Input: seats = [0,1]
    Output: 1

Constraints:
    (1) 2 <= seats.length <= 2 * 10^4
    (2) seats[i] is 0 or 1.
    (3) At least one seat is empty.
    (4) At least one seat is occupied.
"""

class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        occupied = [i for i in range(len(seats)) if seats[i]]
        max_distance = max(occupied[0], len(seats)-1-occupied[-1])
        
        for i in range(1, len(occupied)):
            distance = (occupied[i] - occupied[i-1]) // 2
            if distance > max_distance:
                max_distance = distance
        
        return max_distance