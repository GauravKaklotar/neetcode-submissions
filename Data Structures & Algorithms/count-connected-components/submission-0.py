class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        from collections import defaultdict

        graph = defaultdict(list)

        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        visited = set()

        def dfs(node):
            visited.add(node)

            for nei in graph[node]:
                if nei not in visited:
                    dfs(nei)
        
        ans = 0
        for i in range(n):
            if i not in visited:
                dfs(i)
                ans += 1
        
        return ans
        
