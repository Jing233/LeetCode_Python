class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
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
                queue.append([graph[num], num])
        result = []
        while queue:
            courses, label = queue.pop()
            result.append(label)
            for course in courses:
                inDegree[course] -= 1
                if inDegree[course] == 0:
                    queue.append([graph[course], course])
        
        return result if len(result) == numCourses else []