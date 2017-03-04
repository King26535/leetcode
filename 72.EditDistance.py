class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        #version 242ms
        '''
        m = len(word1)
        n = len(word2)
        if m == 0:
            return n
        if n == 0:
            return m
        dp = [[0]*(m+1) for _ in range(n+1)]
        for i in range(1,m+1):
            dp[0][i] = i
            for j in range(1,n+1):
                dp[j][0] = j
                if word1[i-1] == word2[j-1]:
                    dp[j][i] = dp[j-1][i-1]
                else:
                    dp[j][i] = min(dp[j-1][i-1],dp[j-1][i],dp[j][i-1]) + 1
        return dp[n][m]
        '''
        #version 322ms
        m = len(word1)
        n = len(word2)
        dp = [[0]*(m+1) for _ in range(n+1)]
        for i in range(1,m+1):
            dp[0][i] = i
        for j in range(1,n+1):
            dp[j][0] = j
        for i in range(1,m+1):
            for j in range(1,n+1):
                dp[j][i] = min(dp[j-1][i]+ 1,dp[j][i-1]+ 1,dp[j-1][i-1]+ (0 if word1[i-1] == word2[j-1] else 1)) 
        return dp[n][m]
        
