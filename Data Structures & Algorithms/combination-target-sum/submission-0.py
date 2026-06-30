class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        ans = []
        n = len(nums)

        def solve(i, curr, curr_sum):
            nonlocal ans

            if curr_sum == target:
                ans.append(curr[:])
                return

            if i == n or curr_sum > target:
                return
            
            curr.append(nums[i])
            solve(i, curr, curr_sum + nums[i])
            curr.pop()
            solve(i+1, curr, curr_sum)

        solve(0, [], 0)
        return ans