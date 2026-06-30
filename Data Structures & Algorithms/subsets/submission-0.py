class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        ans = []
        n = len(nums)

        def solve(i, curr):
            nonlocal ans
            if i == n:
                ans.append(curr[:])
                return
            
            curr.append(nums[i])
            
            solve(i+1, curr)

            curr.pop()

            solve(i+1, curr)
        
        solve(0, [])

        return ans