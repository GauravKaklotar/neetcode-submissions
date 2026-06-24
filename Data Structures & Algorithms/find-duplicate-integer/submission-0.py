class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow = nums[0]
        fast = nums[0]

        # Find intersection
        while fast and nums[fast]:
            slow = nums[slow]
            fast = nums[nums[fast]]

            if slow == fast:
                break
        
        # find cycle start point
        slow2 = nums[0]

        while slow != slow2:
            slow = nums[slow]
            slow2 = nums[slow2]
            
        return slow