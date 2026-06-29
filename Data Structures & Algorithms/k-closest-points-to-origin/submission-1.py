class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        import heapq
        hq = []

        for point in points:
            dis = point[0]*point[0] + point[1]*point[1]
            if len(hq) < k:
                heapq.heappush(hq, (-dis, point))
            elif dis < -hq[0][0]:
                heapq.heapreplace(hq, (-dis, point))
        
        ans = [point for _, point in hq]
        return ans