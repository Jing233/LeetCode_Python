class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        
        def dfs(grid, isVisited, x, y):
            if x < 0 or x >= len(grid[0]) or y < 0 or y >= len(grid):
                return 
            
            if isVisited[y][x] or grid[y][x] == '0':
                return
            
            isVisited[y][x] = True
            for dir in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                dfs(grid, isVisited, x + dir[0], y + dir[1])
            
        counter = 0
        isVisited = [[False for _ in range(len(grid[0]))] for _ in range(len(grid))]
        
        for y in xrange(len(grid)):
            for x in xrange(len(grid[0])):
                if grid[y][x] == '1' and not isVisited[y][x]:
                    dfs(grid, isVisited, x, y)
                    counter += 1
        return counter