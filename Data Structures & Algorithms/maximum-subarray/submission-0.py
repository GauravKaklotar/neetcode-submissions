class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        # Kadan's Algo 

        curr_s = nums[0]
        maxi = nums[0]

        for num in nums[1:]:

            curr_s = max(
                num, 
                curr_s + num
            )

            maxi = max(maxi, curr_s)
        
        return maxi