"""
approach: dfs + memoization

you don’t need r < 0 because we never move up or left.
r and c can only increase. they can never become negative.

this problem is a grid, yes, but movement is only: down and right.
so each cell has only 2 choices, not 4.

T.C. O(m*n)
S.C. O(m*n)
"""

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        memo = {}
        def dfs(r,c):
            if r>=m or c>=n:
                return 0
            if r == m-1 and c == n-1:
                return 1

            if (r,c) in memo:
                return memo[(r,c)]
                
            count = 0
            count += dfs(r,c+1)
            count += dfs(r+1,c)

            memo[(r, c)] = count

            return count
        return dfs(0,0)