class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        ans = 0

        directions = [(-1, 0), (0, -1), (1, 0), (0, 1)]
        n, m = len(grid), len(grid[0])

        def solve(i, j):
            grid[i][j] = '0'

            for x, y in directions:
                new_i, new_j = i + x, j + y

                if 0 <= new_i < n and 0 <= new_j < m and grid[new_i][new_j] == '1':
                    solve(new_i, new_j)
        
        for i in range(n):
            for j in range(m):
                if grid[i][j] == "1":
                    ans += 1
                    solve(i, j)
        return ans