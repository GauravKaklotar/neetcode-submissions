class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        nums = sorted(set(nums))
        n = len(nums)

        if n == 0:
            return 0
        
        ans = 1
        start = 0

        for end in range(1, n):
            if nums[end] - nums[end-1] == 1:
                ans = max(ans, end - start + 1)
            else:
                start = end
        
        return ans

                