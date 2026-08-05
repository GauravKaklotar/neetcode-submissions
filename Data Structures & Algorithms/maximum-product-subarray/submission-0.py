class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maxi, mini, ans = nums[0], nums[0], nums[0]

        for num in nums[1:]:
            curr_max = max(num, maxi * num, mini * num)
            curr_min = min(num, maxi * num, mini * num)

            maxi = curr_max
            mini = curr_min

            ans = max(ans, maxi)
        
        return ans