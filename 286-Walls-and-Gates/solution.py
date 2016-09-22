class Solution(object):
    def wallsAndGates(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: void Do not return anything, modify rooms in-place instead.
        """
        from collections import deque
        
        def bfs(toVisit, rooms, depth):
            if len(toVisit) == 0:
                return
            tempToVisit = deque()
            while toVisit:
                i, j = toVisit.popleft()
                for dir in [(0,1), (1,0), (-1,0), (0,-1)]:
                    newI, newJ = i + dir[0], j + dir[1]
                    if 0 <= newI < len(rooms) and 0 <= newJ < len(rooms[0]) and rooms[newI][newJ] > depth:
                        rooms[newI][newJ] = depth
                        tempToVisit.append((newI, newJ))
            bfs(tempToVisit, rooms, depth + 1)
        
        
        
        toVisit = deque()
        for i in range(len(rooms)):
            for j in range(len(rooms[0])):
                if rooms[i][j] == 0:
                    toVisit.append((i, j))
        bfs(toVisit, rooms, 1)
        