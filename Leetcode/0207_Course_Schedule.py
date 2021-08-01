from typing import List

class Solution:
    def dfs(self, graph, v, visited):
        if visited[v] == -1: return False # being visited
        if visited[v] == 1: return True # visited
        
        visited[v] = -1
        for i in graph[v]:
            if not self.dfs(graph, i, visited):
                return False
        
        visited[v] = 1
        return True
    
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        if numCourses == 1: return True
        visited = [0 for _ in range(numCourses)]
        graph = [[] for _ in range(numCourses)]
        for i, j in prerequisites:
            graph[j].append(i)
        
        
        for i in range(numCourses):
            if not self.dfs(graph, i, visited):
                return False # cycled
        return True # non cycled
        