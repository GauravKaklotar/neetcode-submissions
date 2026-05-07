class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ans = 0
        mini = float('inf')

        for x in prices:
            mini = min(x, mini)
            ans = max(ans, x-mini)
        
        return ans