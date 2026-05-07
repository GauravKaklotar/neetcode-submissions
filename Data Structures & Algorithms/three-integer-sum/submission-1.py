class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        nums.sort()
        ans = []
        n = len(nums)

        for i in range(n-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue 

            left = i+1
            right = n-1

            while left < right:

                s = nums[i] + nums[left] + nums[right]

                if s == 0:
                    if [nums[i], nums[left], nums[right]] not in ans:
                        ans.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1
                elif s < 0:
                    left += 1
                else:
                    right -= 1
        
        return ans