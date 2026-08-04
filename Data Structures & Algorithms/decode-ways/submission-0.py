class Solution:
    def numDecodings(self, s: str) -> int:
        
        n = len(s)

        from functools import lru_cache

        @lru_cache(None)
        def solve(i):
            if i == n:
                return 1
            
            if s[i] == '0':
                return 0
            
            # to consider single digit
            ways = solve(i+1)

            # to consider double digit
            if i + 1 < n and 10 <= int(s[i:i+2]) <= 26:
                ways += solve(i+2)
            
            return ways
        
        return solve(0)