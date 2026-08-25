"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        
        intervals.sort(key = lambda x: x.start)

        import heapq

        hq = [] # To keep track of end

        for interval in intervals:
            if hq and hq[0] <= interval.start:
                heapq.heappop(hq)
            heapq.heappush(hq, interval.end)

        return len(hq)