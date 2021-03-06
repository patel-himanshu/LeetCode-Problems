# Question: https://leetcode.com/explore/challenge/card/june-leetcoding-challenge/539/week-1-june-1st-june-7th/3353/

"""
You are given coins of different denominations and a total amount of money. 
Write a function to compute the number of combinations that make up that amount. 
You may assume that you have infinite number of each kind of coin.

Example 1:
    Input: amount = 5, coins = [1, 2, 5]
    Output: 4
    Explanation: There are four ways to make up the amount:
                5=5
                5=2+2+1
                5=2+1+1+1
                5=1+1+1+1+1

Example 2:
    Input: amount = 3, coins = [2]
    Output: 0
    Explanation: the amount of 3 cannot be made up just with coins of 2.

Example 3:
    Input: amount = 10, coins = [10] 
    Output: 1

Note:
    (1) 0 <= amount <= 5000
    (2) 1 <= coin <= 5000
    (3) The number of coins is less than 500
    (4) The answer is guaranteed to fit into signed 32-bit integer
"""

class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        ways = [1]+[0]*amount
        for i in coins:
            for j in range(len(ways)):
                if i <= j:
                    ways[j] += ways[j - i]
        return ways[-1]