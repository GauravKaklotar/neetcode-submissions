class Solution:
    def findMin(self, nums: List[int]) -> int:
        return min(nums)
        left, right = 0, len(nums)
        