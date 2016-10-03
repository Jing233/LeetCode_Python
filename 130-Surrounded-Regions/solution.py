class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        
        
        if not board:
            return
        
        m, n = len(board), len(board[0])
        stack = []
        for i in range(m):
            if board[i][0] == 'O':
                stack.append([i, 0])
            if board[i][n - 1] == 'O':
                stack.append([i, n - 1])
        for j in range(1, n - 1):
            if board[0][j] == 'O':
                stack.append([0, j])
            if board[m - 1][j] == 'O':
                stack.append([m - 1, j])
        
        while stack:
            i, j = stack.pop()
            board[i][j] = '1'
            for dir in [(0,1), (1,0), (-1,0),(0,-1)]:
                newI = i + dir[0]
                newJ = j + dir[1]
                if 0 <= newI < m and 0 <= newJ < n and board[newI][newJ] == 'O':
                    stack.append([newI, newJ])
        
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
        
        for i in range(m):
            for j in range(n):
                if board[i][j] == '1':
                    board[i][j] = 'O'
            