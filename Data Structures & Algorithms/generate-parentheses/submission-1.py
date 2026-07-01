class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        stack = []
        ans = []

        def solve(open, close):
            if open == close == n:
                ans.append("".join(stack[:]))
                return
            
            if open < n:
                stack.append("(")
                solve(open + 1, close)
                stack.pop()
            
            if close < open:
                stack.append(")")
                solve(open, close + 1)
                stack.pop()
            
        solve(0, 0)
        return ans