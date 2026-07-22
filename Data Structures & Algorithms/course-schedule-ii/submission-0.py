class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # ---------------- Kahn's Directed Graph + No Cycle -----------------
        from collections import defaultdict, deque

        graph = defaultdict(list)
        indegree = [0] * numCourses

        for course, pre in prerequisites:
            graph[pre].append(course)
            indegree[course] += 1
        
        q = deque()
        for course in range(numCourses):
            if indegree[course] == 0:
                q.append(course)

        order = []

        while q:

            course = q.popleft()
            order.append(course)

            for nei in graph[course]:
                indegree[nei] -= 1

                if indegree[nei] == 0:
                    q.append(nei)

        if len(order) == numCourses:
            return order
        
        return []