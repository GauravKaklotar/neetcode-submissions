class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        
        from collections import deque

        dq = deque()
        left = 0
        ans = []

        for right in range(len(nums)):

            while dq and nums[right] > nums[dq[-1]]:
                dq.pop()
            
            dq.append(right)

            if dq[0] < left:
                dq.popleft()
            
            if right + 1 >= k:
                ans.append(nums[dq[0]])

                left += 1
        
        return ans
