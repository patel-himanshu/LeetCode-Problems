# Question: https://leetcode.com/explore/featured/card/may-leetcoding-challenge/535/week-2-may-8th-may-14th/3325/

"""
In a town, there are N people labelled from 1 to N.  There is a rumor that one of these people is secretly the town judge.
If the town judge exists, then:
    (1) The town judge trusts nobody.
    (2) Everybody (except for the town judge) trusts the town judge.
    (3) There is exactly one person that satisfies properties 1 and 2.

You are given trust, an array of pairs trust[i] = [a, b] representing that the person labelled a trusts the person labelled b.
If the town judge exists and can be identified, return the label of the town judge.  Otherwise, return -1.

Example 1:
    Input: N = 2, trust = [[1,2]]
    Output: 2

Example 2:
    Input: N = 3, trust = [[1,3],[2,3]]
    Output: 3

Example 3:
    Input: N = 3, trust = [[1,3],[2,3],[3,1]]
    Output: -1

Example 4:
    Input: N = 3, trust = [[1,2],[2,3]]
    Output: -1

Example 5:
    Input: N = 4, trust = [[1,3],[1,4],[2,3],[2,4],[4,3]]
    Output: 3

Constraints:
    (1) 1 <= N <= 1000
    (2) 0 <= trust.length <= 10^4
    (3) trust[i].length == 2
    (4) trust[i] are all different
    (5) trust[i][0] != trust[i][1]
    (6) 1 <= trust[i][0], trust[i][1] <= N
"""

def findJudge(N, trust):
    if N == 1:
        return 1
    
    trusts_on = {}
    trusted_by = {}

    for i in range(1, N+1):
        trusts_on[i] = []
        trusted_by[i] = []

    for i in trust:
        trusts_on[i[0]].append(i[1])
        trusted_by[i[1]].append(i[0])

    for i in range(1, N+1):
        if trusts_on[i] == [] and len(trusted_by[i]) == N-1:
            return i
    return -1

"""
Let a person mentioned on X-axis be 'x', and that on Y-axis be 'y'
Each cross represents that person 'x' is trusted by person 'y'

If a person is town judge, then he must satisfy 2 conditions:
(1) The row along corresponding to that person would be empty
(2) The column corresponding to that person would contain (N-1) crosses

Consider the last example mentioned below.
Person 1: Trusts {2,3,4}, Trusted by {2,3}
Person 2: Trusts {1,3}, Trusted by {1} 
Person 3: Trusts {}, Trusted by {1,2,4}
Person 4: Trusts {1,3}, Trusted by {1}
Hence, person 3 is the town judge
"""

print(findJudge(2, [[1,2]]), end = '\n')
#   1 2
# 1| |X|
# 2| | | <== 2 (Answer)

print(findJudge(3, [[1,3], [2,3]]), end = '\n')
#   1 2 3
# 1| | |X|
# 2| | |X|
# 3| | | | <== 3 (Answer)

print(findJudge(3, [[1,3],[2,3],[3,1]]), end = '\n')
#   1 2 3
# 1| | |X|
# 2| | |X|
# 3|X| | |  -1 (Answer)

print(findJudge(3, [[1,2],[2,3]]), end = '\n')
#   1 2 3
# 1| |X| |
# 2| | |X|
# 3| | | |  -1 (Answer)

print(findJudge(4, [[1,3],[1,4],[2,3],[2,4],[4,3]]), end = '\n')
#   1 2 3 4
# 1| | |X|X|
# 2| | |X|X|
# 3| | | | | <== 3 (Answer) 
# 4| | | |X|

print(findJudge(4, [[1,2],[1,3],[2,1],[2,3],[1,4],[4,3],[4,1]]))
#   1 2 3 4
# 1| |X|X|X|
# 2|X| |X| |
# 3| | | | | <== 3 (Answer)
# 4|X| |X| |