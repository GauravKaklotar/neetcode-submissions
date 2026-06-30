from collections import Counter, deque
import heapq

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:

        count = Counter(tasks)

        heap = [-freq for freq in count.values()]
        heapq.heapify(heap)

        queue = deque()

        time = 0

        while heap or queue:

            time += 1

            # release cooled-down tasks
            if queue and queue[0][1] == time:
                heapq.heappush(heap, queue.popleft()[0])

            # execute one task
            if heap:

                freq = heapq.heappop(heap) + 1

                if freq:
                    queue.append((freq, time + n + 1))

        return time