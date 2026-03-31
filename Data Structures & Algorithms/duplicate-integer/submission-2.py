class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        s = set()

        for num in nums:
            if num in s:
                return True
            else:
                s.add(num)
        
        return False



        # s = set(nums)
        # return len(nums) != len(s)


        # c = Counter(nums)
        # for key, val in c.items():
        #     if val > 1:
        #         return True
        
        # return False