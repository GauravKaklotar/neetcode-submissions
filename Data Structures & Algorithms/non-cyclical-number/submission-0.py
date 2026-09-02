class Solution:
    def isHappy(self, n: int) -> bool:
        
        s = set()

        while n != 1:
            if n in s:
                return False

            s.add(n)
            curr = 0
            while n > 0:
                digit = n % 10
                curr += digit * digit
                n //= 10
            
            n = curr
        
        return True