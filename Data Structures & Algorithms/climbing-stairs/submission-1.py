class Solution:
    def climbStairs(self, n: int) -> int:
        
        from functools import lru_cache

        @lru_cache(None)
        def solve(x):
            if x == 0:
                return 0
            elif x == 1 or x == 2:
                return x
            return solve(x-1) + solve(x-2)
        
        return solve(n)