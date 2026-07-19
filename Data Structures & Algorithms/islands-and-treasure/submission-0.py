class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        
        inf = 2147483647
        n, m = len(grid), len(grid[0])

        from collections import deque

        q = deque([])

        for i in range(n):
            for j in range(m):
                # Append all the treasure
                if grid[i][j] == 0:
                    q.append((i, j))
        
        directions = [
            (-1,0),
            (1,0),
            (0,-1),
            (0,1)
        ]

        # At each step expand from treasure to land
        while q:
            r, c = q.popleft()

            for x, y in directions:
                nr, nc = r + x, c + y

                if 0 <= nr < n and 0 <= nc < m and grid[nr][nc] == inf:
                    grid[nr][nc] = grid[r][c] + 1
                    q.append((nr, nc))



