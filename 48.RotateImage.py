class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        '''
        # left rotate
        n = len(matrix)
        l = n/2 if n%2 == 0 else n/2+1
        r = n/2
        for i in range(l):
            for j in range(r):
                temp1 = matrix[i][j]
                temp2 = matrix[j][n-1-i]
                temp3 = matrix[n-1-i][n-1-j]
                matrix[n-1-i][n-1-j] = matrix[n-1-j][i]
                matrix[n-1-j][i] = temp1
                matrix[i][j] = temp2
                matrix[j][n-1-i] = temp3
        return
        '''
        '''
        # myself
        # right rotate 43ms
        n = len(matrix)
        for i in xrange(n/2):
            for j in xrange(n-n/2):
                temp1 = matrix[i][j]
                temp2 = matrix[j][n-1-i]
                temp3 = matrix[n-1-i][n-1-j]
                matrix[i][j] = matrix[n-1-j][i]
                matrix[n-1-j][i] = temp3
                matrix[n-1-i][n-1-j] = temp2
                matrix[j][n-1-i] = temp1
        return
        '''
        '''
        # 62ms
        matrix.reverse()
        for i in range(len(matrix)):
            for j in range(i+1,len(matrix)):
                temp = matrix[i][j]
                matrix[i][j] = matrix[j][i]
                matrix[j][i] = temp
        '''
        '''
        #62ms
        matrix.reverse()
        for i in range(len(matrix)):
            for j in range(i):
                matrix[i][j],matrix[j][i] = matrix[j][i],matrix[i][j]
        '''
        '''
        # 49ms
        matrix[:] = [[row[i] for row in matrix[::-1]] for i in range(len(matrix))]
        '''
        #49ms
        n = len(matrix)
        for i in xrange(n/2):
            for j in xrange(n-n/2):
                 matrix[i][j], matrix[~j][i], matrix[~i][~j], matrix[j][~i] = matrix[~j][i], matrix[~i][~j], matrix[j][~i], matrix[i][j]
                
