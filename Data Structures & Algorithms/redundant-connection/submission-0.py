class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        # 2 Solutions 
        # Union Find
        # ------------ DFS ------------------

        from collections import defaultdict

        graph = defaultdict(list)

        # Logic: Before adding edge we'll check if there's a way to reach from u --> v then return that [u, v] as it'll create cycle

        def dfs(src, target, visited):
            if src == target:
                return True
            
            visited.add(src)

            for nei in graph[src]:
                if nei not in visited:
                    if dfs(nei, target, visited):
                        return True

            return False
        

        for u, v in edges:
            if u in graph and v in graph:
                if dfs(u, v, set()):
                    return [u, v]

            graph[u].append(v)
            graph[v].append(u)