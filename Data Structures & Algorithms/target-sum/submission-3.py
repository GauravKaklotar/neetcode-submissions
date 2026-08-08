class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        
        total = sum(nums)
        n = len(nums)

        if abs(target) > total:
            return 0

        if (target + total) % 2 != 0:
            return 0
        
        from functools import lru_cache

        @lru_cache(None)
        def solve(i, curr):
            if i == n:
                return 1 if curr == 0 else 0
            
            if i >= n:
                return 0
            
            ans = 0
            if curr >= nums[i]:
                ans += solve(i+1, curr - nums[i])
            
            ans += solve(i+1, curr)

            return ans
        
        return solve(0, (target + total) // 2)