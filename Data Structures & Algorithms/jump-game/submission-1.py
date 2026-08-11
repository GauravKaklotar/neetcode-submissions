class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # -------- Greedy ------------
        n = len(nums)

        farthest = 0

        for i in range(n):
            if i > farthest:
                return False
            
            farthest = max(farthest, i + nums[i])

            if farthest >= n-1:
                return True
        
        return True


        # --------- Recursive + Memo -----------------
        # n = len(nums)

        # from functools import lru_cache

        # @lru_cache(None)
        # def solve(i):
        #     if i>=n-1:
        #         return True
            
        #     for jump in range(1, nums[i] + 1):
        #         if solve(i + jump):
        #             return True

        #     return False
        
        # return solve(0)