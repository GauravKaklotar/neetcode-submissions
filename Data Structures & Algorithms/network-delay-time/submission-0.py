class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        
        from collections import defaultdict
        import heapq

        graph = defaultdict(list)

        for u, v, t in times:
            graph[u].append((v, t))
        
        hq = [(0, k)]
        visited = set()
        
        ans = 0

        while hq:

            dist, node = heapq.heappop(hq)

            if node in visited:
                continue
            
            ans = dist
            visited.add(node)

            for nei, t in graph[node]:
                if nei not in visited:
                    heapq.heappush(hq, (dist + t, nei))
        
        return ans if len(visited) == n else -1