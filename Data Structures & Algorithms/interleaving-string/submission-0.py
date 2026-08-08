class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        
        n, m = len(s1), len(s2)

        if n + m != len(s3):
            return False
        
        from functools import lru_cache

        @lru_cache(None)
        def solve(i, j):

            if i == n and j == m:
                return True

            k = i + j

            if i < n and s1[i] == s3[k]:
                if solve(i+1, j):
                    return True
                
            if j < m and s2[j] == s3[k]:
                if solve(i, j+1):
                    return True

            return False
        return solve(0, 0)