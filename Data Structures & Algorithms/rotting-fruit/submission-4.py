class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        from collections import deque

        q = deque([])
        n, m = len(grid), len(grid[0])
        fresh = 0

        # Collect all rotten fruit
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 2:
                    q.append((i, j))
                elif grid[i][j] == 1:
                    fresh += 1
                
        directions = [
            (-1,0),
            (1,0),
            (0,-1),
            (0,1)
        ]

        ans = 0
        while q:
            
            current_len = len(q)

            for _ in range(current_len):
                r, c = q.popleft()

                for x, y in directions:
                    nr, nc = r + x, c + y

                    if 0 <= nr < n and 0 <= nc < m and grid[nr][nc] == 1:
                        fresh -= 1
                        grid[nr][nc] = 2
                        q.append((nr, nc))
            ans += 1
        
        if fresh != 0:
            return -1
        
        return ans - 1 if ans else 0


