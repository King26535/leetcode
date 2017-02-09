class Solution(object):
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        self.solve(board)
    ''' 
    def solve(self,board):
        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    for char in '123456789':
                        if self.valid(board,i,j,char):
                            board[i][j] = char
                            if self.solve(board):
                                return True
                            else:
                                board[i][j] = '.'
                    return False
        return True
        
    def valid(self,board,i,j,char):
        for row in range(9):
            if board[row][j] == char:
                return False
        
        for col in range(9):
            if board[i][col] == char:
                return False
                
        for k in range(i/3*3,i/3*3+3):
            for l in range(j/3*3,j/3*3+3):
                if board[k][l] == char:
                    return False
        return True
    '''
    def solve(self,board):
        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    for char in '123456789':
                        board[i][j] = char
                        if self.valid(board,i,j) and self.solve(board):
                            return True
                        board[i][j] = '.'
                    return False
        return True
        
    def valid(self,board,i,j):
        temp = board[i][j]
        board[i][j] = '.'
        for row in range(9):
            if board[row][j] == temp:
                return False
        
        for col in range(9):
            if board[i][col] == temp:
                return False
                
        for k in range(i/3*3,i/3*3+3):
            for l in range(j/3*3,j/3*3+3):
                if board[k][l] == temp:
                    return False
        board[i][j] = temp
        return True
