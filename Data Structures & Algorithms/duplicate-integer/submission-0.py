class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        c = Counter(nums)
        for key, val in c.items():
            if val > 1:
                return True
        
        return False