class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        '''
        #version1.0
        m = len(grid)
        n = len(grid[0])
        for i in range(1,n):
            grid[0][i] += grid[0][i-1]
        for j in range(1,m):
            grid[j][0] += grid[j-1][0]
        for i in range(1,n):
            for j in range(1,m):
                grid[j][i] = min(grid[j-1][i],grid[j][i-1]) + grid[j][i]
        return grid[m-1][n-1]
        '''
        #version 2.0 recode the min path
        m = len(grid)
        n = len(grid[0])
        dp = [[0]*n for _ in range(m)]
        dp[0][0] = 1
        for i in range(1,n):
            grid[0][i] += grid[0][i-1]
        for j in range(1,m):
            grid[j][0] += grid[j-1][0]
        for i in range(1,n):
            for j in range(1,m):
                grid[j][i] = min(grid[j-1][i],grid[j][i-1]) + grid[j][i]
                if grid[j-1][i] < grid[j][i-1]:
                    dp[j-1][i] = 1
                else:
                    dp[j][i-1] = 1
        return grid[m-1][n-1]
                    
