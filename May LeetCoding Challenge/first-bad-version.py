# Question: https://leetcode.com/explore/featured/card/may-leetcoding-challenge/534/week-1-may-1st-may-7th/3316/

"""
You are a product manager and currently leading a team to develop a new product. 
Unfortunately, the latest version of your product fails the quality check.
Since each version is developed based on the previous version, all the versions after a bad version are also bad.
Suppose you have n versions [1, 2, ..., n] and you want to find out the first bad one, which causes all the following ones to be bad.
You are given an API bool isBadVersion(version) which will return whether version is bad. 
Implement a function to find the first bad version. You should minimize the number of calls to the API.

Example:
    Given n = 5, and version = 4 is the first bad version.

    call isBadVersion(3) -> false
    call isBadVersion(5) -> true
    call isBadVersion(4) -> true

    Then 4 is the first bad version. 
"""

from math import sqrt

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """        
        for i in range(n,-1,-round(sqrt(n))):
            if i<0:
                break
            elif isBadVersion(i)==0:
                while 1:
                    i+=1
                    if isBadVersion(i):
                        return i
        i = 0
        while 1:
            i+=1
            if isBadVersion(i):
                return i