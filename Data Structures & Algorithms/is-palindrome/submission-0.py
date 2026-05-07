class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        import re

        s = re.findall(r"[a-zA-Z0-9]", s)
        s = "".join(s).lower()
        return s == s[::-1]
        