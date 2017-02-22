class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        '''
        #version 1.0
        if n == 0:
            return []
        res = [[0]*n for i in range(n)]
        ans = 0
        rowStart,rowEnd,colStart,colEnd = 0,n-1,0,n-1
        while rowStart <= rowEnd and colStart <= colEnd:
            for i in range(colStart,colEnd + 1):
                ans += 1
                res[rowStart][i] = ans
            rowStart += 1
            
            for j in range(rowStart,rowEnd + 1):
                ans += 1
                res[j][colEnd] = ans
            colEnd -= 1
            
            for i in range(colEnd,colStart-1,-1):
                ans += 1
                res[rowEnd][i] = ans
            rowEnd -= 1
            
            for j in range(rowEnd,rowStart-1,-1):
                ans += 1
                res[j][colStart] = ans
            colStart += 1
        return res
        '''
        #version 2.0
        res = [[0]*n for i in range(n)]
        i,j,di,dj = 0,0,0,1
        for k in range(1,n*n+1):
            res[i][j] = k
            if res[(i+di)%n][(j+dj)%n]:
                di, dj = dj, -di
            i += di
            j += dj
        return res
