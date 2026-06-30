class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        used = set()
        path = []
        ans = []

        def dfs():
            nonlocal used, path, ans

            if len(path) == len(nums):
                ans.append(path[:])
                return
            
            for num in nums:
                if num in used:
                    continue
                
                path.append(num)
                used.add(num)

                dfs()

                path.pop()
                used.remove(num)
            
        dfs()
        return ans