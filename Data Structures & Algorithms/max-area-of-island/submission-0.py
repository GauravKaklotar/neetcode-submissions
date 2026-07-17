class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ans = 0

        directions = [(-1, 0), (0, -1), (1, 0), (0, 1)]
        n, m = len(grid), len(grid[0])

        def solve(i, j):
            grid[i][j] = 0

            area = 1

            for x, y in directions:
                new_i, new_j = i + x, j + y

                if 0 <= new_i < n and 0 <= new_j < m and grid[new_i][new_j] == 1:
                    area += solve(new_i, new_j)
            
            return area
        
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    ans = max(ans, solve(i, j))
                    
        return ans