class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        from functools import lru_cache

        n = len(s)

        @lru_cache(None)
        def solve(i):
            if i == n:
                return True
            
            for word in wordDict:
                if s[i:i+len(word)] == word:
                    if solve(i+len(word)):
                        return True
            
            return False

        return solve(0)