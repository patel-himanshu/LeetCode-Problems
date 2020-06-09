# Question: https://leetcode.com/explore/challenge/card/june-leetcoding-challenge/540/week-2-june-8th-june-14th/3355/

"""
Given a string s and a string t, check if s is subsequence of t.
A subsequence of a string is a new string which is formed from the original string by 
deleting some (can be none) of the characters without disturbing the relative positions
 of the remaining characters. (ie, "ace" is a subsequence of "abcde" while "aec" is not).

Follow up:
If there are lots of incoming S, say S1, S2, ... , Sk where k >= 1B, and you want to check 
one by one to see if T has its subsequence. In this scenario, how would you change your code?

Example 1:
    Input: s = "abc", t = "ahbgdc"
    Output: true

Example 2:
    Input: s = "axc", t = "ahbgdc"
    Output: false

Constraints:
    (1) 0 <= s.length <= 100
    (2) 0 <= t.length <= 10^4
    (3) Both strings consists only of lowercase characters.
"""

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s)==0:
            return True
        elif len(t)==0:
            return False
        
        i,j = 0,0
        while i<len(s) and j<len(t):
            if s[i] == t[j]:
                i += 1
            j += 1
        
        return i==len(s)