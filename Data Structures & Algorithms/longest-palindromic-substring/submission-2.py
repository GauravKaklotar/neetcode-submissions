class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        n = len(s)
        start = 0

        dp = [False] * n
        max_len = 1

        for i in range(n-1, -1, -1):
            for j in range(n-1, i-1, -1):
                
                # Checking for j-i <= 2 to consider odd/even length of palindrome
                if s[i] == s[j] and (j-i <= 2 or dp[j-1]):
                    dp[j] = True

                    if j - i + 1 > max_len:
                        start = i
                        max_len = j - i + 1
                else:
                    dp[j] = False
        
        return s[start:start + max_len]