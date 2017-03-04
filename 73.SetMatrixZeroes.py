class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        '''
        #version 1.0 165ms
        row, col = [],[]
        m,n = len(matrix),len(matrix[0])
        for i in xrange(m):
            for j in xrange(n):
                if matrix[i][j] == 0:
                    if i not in row:
                        row.append(i)
                    if j not in col:
                        col.append(j)
        for i in row:
            for j in xrange(n):
                matrix[i][j] = 0
        for j in col:
            for i in xrange(m):
                matrix[i][j] = 0
        '''
        #version 2.0 189ms
        col0,m,n = 1,len(matrix),len(matrix[0])
        for i in xrange(m):
            if matrix[i][0] == 0:
                col0 = 0
            for j in xrange(1,n):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0
        for i in xrange(m-1,-1,-1):
            for j in xrange(n-1,0,-1):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0
            if col0 == 0:
                matrix[i][0] = 0
