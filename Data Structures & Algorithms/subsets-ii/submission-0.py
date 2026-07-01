class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        
        nums.sort()
        ans = []
        curr = []

        def solve(i):
            nonlocal ans, curr

            if i == len(nums):
                ans.append(curr[:])
                return
            
            # take
            curr.append(nums[i])
            solve(i+1)
            curr.pop()

            # Not-take and skip duplicate elements
            while i + 1 < len(nums) and nums[i] == nums[i+1]:
                i+=1
            
            solve(i+1)
        
        solve(0)
        return ans