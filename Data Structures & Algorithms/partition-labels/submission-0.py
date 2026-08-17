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