class Solution:
    def climbStairs(self, n: int) -> int:
        #1. supproblem: ways(n) where ways(n) represents num disticnt waysto climb to the top of staircase: 
        #2. Recurrence: ways(n) = ways(n-1) + ways(n-2)
        #3. Basecase: ways[1] = 1, ways[2] = 2
        ways = [0,1,2]
        for i in range(3,n+1):
            ways.append(ways[i-1] + ways[i-2])
        return ways[n]

        