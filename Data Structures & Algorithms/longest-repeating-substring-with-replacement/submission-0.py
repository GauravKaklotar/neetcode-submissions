class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}

        ans = 0
        left = 0
        max_f = 0

        for right in range(len(s)):
            count[s[right]] = count.get(s[right], 0) + 1

            max_f = max(max_f, count[s[right]])

            window_size = right - left + 1

            while window_size - max_f > k:
                count[s[left]] -= 1
                left += 1
                window_size -= 1

            ans = max(ans, window_size)
        
        return ans