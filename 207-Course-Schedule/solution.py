class graphNode(object):
    def __init__(self, label=None, neighbors=None):
        self.label = label
        self.neighbors = neighbors

class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        import collections
        
        graph = [[] for i in range(numCourses)]
        for course, pre in prerequisites:
            graph[pre].append(course)
        
        inDegree = [0] * numCourses
        for course in graph:
            for nei in course:
                inDegree[nei] += 1
        
        queue = collections.deque()
        for num in range(numCourses):
            if inDegree[num] == 0:
                queue.append(graph[num])
        cnt = 0
        while queue:
            courses = queue.pop()
            cnt += 1
            for course in courses:
                inDegree[course] -= 1
                if inDegree[course] == 0:
                    queue.append(graph[course])
        
        return cnt == numCourses
                
            