class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        
        n, m = len(text1), len(text2)

        from functools import lru_cache

        @lru_cache(None)
        def solve(i, j):
            if i<=0 or j<=0:
                return 0
            
            ans = 0
            if text1[i-1] == text2[j-1]:
                ans += 1 + solve(i-1, j-1)
            else:
                ans += max(solve(i-1, j), solve(i, j-1))
            
            return ans

        return solve(n, m)