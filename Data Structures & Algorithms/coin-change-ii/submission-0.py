class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        
        n = len(coins)

        from functools import lru_cache

        @lru_cache(None)
        def solve(i, curr):
            if curr == 0:
                return 1
            
            if i >= n:
                return 0
            
            ans = 0

            if curr >= coins[i]:
                ans += solve(i, curr - coins[i])
            
            ans += solve(i+1, curr)
            return ans
        
        return solve(0, amount)