class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        s = set(nums)
        return len(nums) != len(s)


        # c = Counter(nums)
        # for key, val in c.items():
        #     if val > 1:
        #         return True
        
        # return False