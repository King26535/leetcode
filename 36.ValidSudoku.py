class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        row = [[0 for i in range(len(board[0]))] for j in range(len(board))]
        col = [[0 for i in range(len(board[0]))] for j in range(len(board))]
        block = [[0 for i in range(len(board[0]))] for j in range(len(board))]
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == '.':
                    continue
                
                cur = int(board[i][j]) - 1
                block_tmp = i/3*3 + j/3
                if row[cur][i] or col[cur][j] or block[cur][block_tmp]:
                    return False
                else:
                    row[cur][i] = 1
                    col[cur][j] = 1
                    block[cur][block_tmp] = 1
        return True
