import heapq

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.hq = []
        for num in nums:
            heapq.heappush(self.hq, num)
            if len(self.hq) > self.k:
                heapq.heappop(self.hq)

    def add(self, val: int) -> int:
        heapq.heappush(self.hq, val)
        if len(self.hq) > self.k:
            heapq.heappop(self.hq)
        res = self.hq[0]
        return res
