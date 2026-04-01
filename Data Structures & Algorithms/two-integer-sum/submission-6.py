class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)

        d = dict()

        for i, num in enumerate(nums):
            if num in d:
                prev_ind, count = d[num]
                d[num] = (i, count+1)
            else:
                d[num] = (i, 1)
        
        print(d)
        for i, num in enumerate(nums):
            val = target - num
            if val in d:
                index, count = d[val]
                if val == num:
                    if count > 1:
                        return [i, index]
                    else:
                        continue
                
                return [i, index]
                
        


        # Time : O(n**2)
        # Space: O(1)
                    