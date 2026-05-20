class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        last_seen = dict()
        ans = 0
        left = 0

        for right in range(len(s)):
            ch = s[right]

            if ch in last_seen and last_seen[ch] >= left:
                left = last_seen[ch] + 1
            
            last_seen[ch] = right
            ans = max(ans, right - left + 1)
        
        return ans
