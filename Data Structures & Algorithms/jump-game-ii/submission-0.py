class Solution:
    def jump(self, nums: List[int]) -> int:
        
        left, right = 0, 0
        jump = 0

        while right < len(nums) - 1:
            farthest = right

            for i in range(left, right + 1):
                farthest = max(
                    farthest,
                    i + nums[i]
                )
            
            left = right + 1
            right = farthest
            jump += 1

        return jump