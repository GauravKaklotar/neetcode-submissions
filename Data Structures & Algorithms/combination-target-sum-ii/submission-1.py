class Solution:
    def combinationSum2(self, nums: List[int], target: int) -> List[List[int]]:
        ans = []
        nums.sort()
        n = len(nums)

        def solve(i, curr, curr_sum):
            nonlocal ans

            if curr_sum == target:
                res = curr[:]
                if res not in ans:
                    ans.append(res)
                return

            if i == n or curr_sum > target:
                return
            
            # take
            curr.append(nums[i])
            solve(i+1, curr, curr_sum + nums[i])
            curr.pop()

            # Ignore duplicate branches for explore
            j = i+1
            while j < n and nums[j] == nums[i]:
                j+=1

            solve(j, curr, curr_sum)

        solve(0, [], 0)
        return ans