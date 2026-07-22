class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # DFS
        from collections import defaultdict

        graph = defaultdict(list)

        for course, pre in prerequisites:
            graph[pre].append(course)
        
        state = [0] * numCourses
        # 0 --> unvisited
        # 1 --> visiting
        # 2 --> visited

        def dfs(course):

            if state[course] == 1:
                return False

            if state[course] == 2:
                return True
            
            state[course] = 1

            for nei in graph[course]:
                if not dfs(nei):
                    return False
            
            state[course] = 2
            
            return True
        
        for course in range(numCourses):
            if not dfs(course):
                return False
        
        return True
