class Solution:

    def encode(self, strs: List[str]) -> str:
        parts = []
        for s in strs:
            parts.append(f"{len(s)}#{s}")
        return "".join(parts)

    def decode(self, s: str) -> List[str]:
        ans = []
        i = 0
        
        while i < len(s):
            # Find the '#' delimiter
            j = i
            while j < len(s) and s[j] != '#':
                j += 1
                
            length = int(s[i:j])
            
            string = s[j+1: j+1+length]
            ans.append(string)
            
            i = j + 1 + length
        
        return ans