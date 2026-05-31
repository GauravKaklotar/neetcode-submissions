class Solution:
    def dailyTemperatures(self, l: List[int]) -> List[int]:
        n = len(l)
        res = [0] * n
        stack = []

        for i in range(n):

            while stack and l[i] > l[stack[-1]]:
                prev_idx = stack.pop()
                res[prev_idx] = i - prev_idx
            
            stack.append(i)

        return res

