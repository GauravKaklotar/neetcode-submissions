class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        # 2 Solutions 
        # Union Find
        n = len(edges)

        parent = [i for i in range(n+1)]
        rank = [1] * (n+1)

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            
            return parent[x]
        
        def union(x, y):
            rootX, rootY = find(x), find(y)

            # Cycle detected
            if rootX == rootY:
                return False
            
            # Attach smaller tree under larger tree
            if rank[rootX] > rank[rootY]:
                parent[rootY] = rootX
            elif rank[rootX] < rank[rootY]:
                parent[rootX] = rootY
            else:
                parent[rootY] = rootX
                rank[rootX] += 1
            
            return True

        for u, v in edges:
            if not union(u, v):
                return [u, v]

            
        # ------------ DFS ------------------

        # from collections import defaultdict

        # graph = defaultdict(list)

        # # Logic: Before adding edge we'll check if there's a way to reach from u --> v then return that [u, v] as it'll create cycle

        # def dfs(src, target, visited):
        #     if src == target:
        #         return True
            
        #     visited.add(src)

        #     for nei in graph[src]:
        #         if nei not in visited:
        #             if dfs(nei, target, visited):
        #                 return True

        #     return False
        

        # for u, v in edges:
        #     if u in graph and v in graph:
        #         if dfs(u, v, set()):
        #             return [u, v]

        #     graph[u].append(v)
        #     graph[v].append(u)