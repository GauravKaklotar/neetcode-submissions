class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)

        from functools import lru_cache

        @lru_cache(None)
        def solve(i, buy):
            if i>=n:
                return 0
            
            ans = 0
            if buy:
                ans = max(-prices[i] + solve(i+1, False),
                                0    + solve(i+1, True))
            else:
                ans = max(prices[i] + solve(i+2, True),
                                0    + solve(i+1, False))
            
            return ans
        
        return solve(0, True)