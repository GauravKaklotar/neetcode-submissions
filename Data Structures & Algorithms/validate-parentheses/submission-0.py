class Solution:
    def isValid(self, s: str) -> bool:
        l = []
        d = {
            ')' : '(',
            ']' : '[',
            '}' : '{'
        }

        for br in s:
            if br in "({[":
                l.append(br)
            else:
                if l and (l[-1] == d[br]):
                    l.pop()
                else:
                    return False
        
        return len(l)==0