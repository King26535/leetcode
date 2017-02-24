class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        '''
        #version 1.0
        N = m+n-2
        k = m-1
        res = 1.0
        for i in range(1,m):
            res = res*(N-k+i)/i
        return int(res)
        '''
        '''
        #version 2.0
        dp = [[1 if i == 0 or j == 0 else 1 for i in range(n)] for j in range(m)]
        for i in range(1,n):
            for j in range(1,m):
                dp[j][i] = dp[j-1][i] + dp[j][i-1]
        return dp[m-1][n-1]
        '''
        '''
        #version 3.0
        cur = [1]*m
        for i in range(n-1):
            for j in range(1,m):
                cur[j] += cur[j-1]
        return cur[m-1]
        '''
        #version 4.0
        dp = [[0]*(n+1) for j in range(m+1)]
        dp[0][1] = 1
        for i in range(1,n+1):
            for j in range(1,m+1):
                dp[j][i] = dp[j-1][i] + dp[j][i-1]
        return dp[m][n]
