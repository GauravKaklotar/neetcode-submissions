class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        
        last = {}

        for i, char in enumerate(s):
            last[char] = i
        
        start = 0
        end = 0
        ans = []

        for i in range(len(s)):
            end = max(end, last[s[i]])

            if i == end:
                ans.append(end - start + 1)
                start = end + 1
        
        return ans

'''
Why is this greedy?

At every position, we maintain the furthest boundary required by the characters we've seen.

Current partition
       ↓
character appears later
       ↓
extend boundary
       ↓
all characters contained?
       ↓
YES → cut immediately
'''