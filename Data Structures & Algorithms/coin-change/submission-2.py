class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # ------------------ bottom-up ------------------------- 
        n = len(coins)

        dp = [float('inf')] * (amount + 1)

        # 0 coins are needed to make amount 0
        dp[0] = 0

        for a in range(1, amount + 1):
            for coin in coins:
                # If the coin is smaller or equal to the current amount
                if a - coin >= 0:
                    dp[a] = min(dp[a], 1 + dp[a - coin])
        
        return dp[amount] if dp[amount] != float('inf') else -1
        



        # ----------------TLE without setrecursionlimit---------------------
        
        # n = len(coins)

        # from functools import lru_cache
        # import sys

        # sys.setrecursionlimit(10**8)
        # dp = {}
        # # @lru_cache(None)
        # def solve(curr):
        #     if curr == 0:
        #         return 0
            
        #     if curr < 0:
        #         return float('inf')
            
        #     if dp.get(curr, 0):
        #         return dp[curr]
            
        #     ans = float('inf')

        #     for coin in coins:
        #         ans = min(
        #             ans, 
        #             1 + solve(curr - coin)
        #         )
            
        #     dp[curr] = ans
        #     return ans

        # result = solve(amount)

        # return result if result != float("inf") else -1