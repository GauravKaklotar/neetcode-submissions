class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        n = len(cost)

        from functools import lru_cache

        @lru_cache(None)
        def solve(i):

            if i >= n:
                return 0

            return cost[i] + min(
                solve(i + 1),
                solve(i + 2)
            )

        
        return min(solve(0), solve(1))
