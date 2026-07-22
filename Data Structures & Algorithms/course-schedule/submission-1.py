class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
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

        finished = 0

        while q:

            course = q.popleft()
            finished += 1

            for nei in graph[course]:
                indegree[nei] -= 1

                if indegree[nei] == 0:
                    q.append(nei)

        return finished == numCourses

        # ---------------- DFS Directed Graph + No Cycle -----------------
        # from collections import defaultdict

        # graph = defaultdict(list)

        # for course, pre in prerequisites:
        #     graph[pre].append(course)
        
        # state = [0] * numCourses
        # # 0 --> unvisited
        # # 1 --> visiting
        # # 2 --> visited

        # def dfs(course):

        #     if state[course] == 1:
        #         return False

        #     if state[course] == 2:
        #         return True
            
        #     state[course] = 1

        #     for nei in graph[course]:
        #         if not dfs(nei):
        #             return False
            
        #     state[course] = 2
            
        #     return True
        
        # for course in range(numCourses):
        #     if not dfs(course):
        #         return False
        
        # return True
