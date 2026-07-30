from functools import lru_cache

class Solution:
    def rob(self, nums: List[int]) -> int:

        n = len(nums)

        @lru_cache(None)
        def solve(i):

            if i >= n:
                return 0

            rob = nums[i] + solve(i + 2)
            skip = solve(i + 1)

            return max(rob, skip)

        return solve(0)