class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        n = len(coins)

        from functools import lru_cache
        import sys

        sys.setrecursionlimit(10**8)
        dp = {}
        # @lru_cache(None)
        def solve(curr):
            if curr == 0:
                return 0
            
            if curr < 0:
                return float('inf')
            
            if dp.get(curr, 0):
                return dp[curr]
            
            ans = float('inf')

            for coin in coins:
                ans = min(
                    ans, 
                    1 + solve(curr - coin)
                )
            
            dp[curr] = ans
            return ans

        result = solve(amount)

        return result if result != float("inf") else -1