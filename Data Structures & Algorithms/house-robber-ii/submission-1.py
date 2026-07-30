from functools import lru_cache

class Solution:
    def rob(self, nums: List[int]) -> int:
        
        if len(nums) == 1:
            return nums[0]
            
        def helper(nums):

            n = len(nums)   

            @lru_cache(None)
            def solve(i):

                if i >= n:
                    return 0

                rob = nums[i] + solve(i + 2)
                skip = solve(i + 1)

                return max(rob, skip)

            return solve(0)
        
        '''
        Every valid robbery must satisfy one of these:

            - Doesn't rob the first house ✅
            - Doesn't rob the last house ✅

        There is no third possibility, because robbing both is illegal.
        '''
        return max(
            helper(nums[:-1]),
            helper(nums[1:])
        )