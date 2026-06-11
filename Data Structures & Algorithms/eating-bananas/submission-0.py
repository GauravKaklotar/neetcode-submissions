class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        import math
        def check(k):
            count = 0
            for x in piles:
                count += math.ceil(x / k)
            
            return count <= h

        left = 1
        right = max(piles)

        while left <= right:
            mid = (left + right) // 2
            if check(mid):
                right = mid - 1
            else:
                left = mid + 1
        
        return left

