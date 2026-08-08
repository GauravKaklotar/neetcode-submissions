from functools import lru_cache

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:

        m = len(word1)
        n = len(word2)

        @lru_cache(None)
        def solve(i, j):

            if i == m:
                return n - j

            if j == n:
                return m - i

            if word1[i] == word2[j]:
                return solve(i + 1, j + 1)

            insert = 1 + solve(i, j + 1)
            delete = 1 + solve(i + 1, j)
            replace = 1 + solve(i + 1, j + 1)

            return min(insert, delete, replace)

        return solve(0, 0)