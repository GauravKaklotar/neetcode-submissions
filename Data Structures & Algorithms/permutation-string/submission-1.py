class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        win_size = len(s1)
        c1 = dict(Counter(s1))
        current = dict(Counter(s2[:win_size]))

        left = 0

        for right in range(win_size, len(s2)):
            if c1 == current:
                return True
            
            if s2[right] in current:
                current[s2[right]] += 1
            else:
                current[s2[right]] = 1
            current[s2[left]] -= 1
            if current[s2[left]] == 0:
                del current[s2[left]]
            left += 1
        
        return c1 == current
        
