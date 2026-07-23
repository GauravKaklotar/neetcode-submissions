class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows, cols = len(heights), len(heights[0])

        pacific = set()
        atlantic = set()

        directions = [
            (-1, 0),
            (1, 0),
            (0, -1),
            (0, 1)
        ]

        def dfs(r, c, visited):

            visited.add((r, c))

            for dr, dc in directions:

                nr = r + dr
                nc = c + dc

                if (
                    0 <= nr < rows and
                    0 <= nc < cols and
                    (nr, nc) not in visited and
                    heights[nr][nc] >= heights[r][c]
                ):
                    dfs(nr, nc, visited)

        # Pacific (top row)
        for c in range(cols):
            dfs(0, c, pacific)

        # Pacific (left column)
        for r in range(rows):
            dfs(r, 0, pacific)

        # Atlantic (bottom row)
        for c in range(cols):
            dfs(rows - 1, c, atlantic)

        # Atlantic (right column)
        for r in range(rows):
            dfs(r, cols - 1, atlantic)

        ans = []

        for r in range(rows):
            for c in range(cols):
                if (r, c) in pacific and (r, c) in atlantic:
                    ans.append([r, c])

        return ans



'''
Pacific borders
      │
      ▼
Reverse DFS
      │
      ▼
Cells reachable from Pacific


Atlantic borders
      │
      ▼
Reverse DFS
      │
      ▼
Cells reachable from Atlantic


Intersection
      │
      ▼
Answer


Algorithm
Create two sets:
    pacific → cells that can reach the Pacific.
    atlantic → cells that can reach the Atlantic.
Run DFS from:
    Pacific borders (top row + left column)
    Atlantic borders (bottom row + right column)
During DFS, move only to cells with:
    next_height >= current_height

because we're traversing the water flow in reverse.
The answer is the intersection of the two sets.
'''