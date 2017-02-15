class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        '''
        #version 1.0 142ms
        i,j,ss,star = 0,0,0,-1
        while i < len(s):
            if j < len(p) and (p[j] == '?' or s[i] == p[j]):
                i += 1
                j += 1
                continue
            if j < len(p) and p[j] == '*':
                ss = i
                star = j
                j += 1
                continue
            if star != -1:
                ss += 1
                i = ss
                j = star + 1
                continue
            return False
        while j < len(p) and p[j] == '*':
            j += 1
        return j == len(p)
        '''
        '''
        #version 2.0 dp 1132ms
        count = 0
        for char in p:
            if char == '*':
                count += 1
        if len(p) - count > len(s):
            return False
        dp = [[False for i in range(len(p)+1)] for j in range(len(s)+1)]
        dp[0][0] = True
        for j in range(1,len(p)+1):
            dp[0][j] = dp[0][j-1] and p[j-1] == '*'
        for i in range(1,len(s)+1):
            for j in range(1,len(p)+1):
                if p[j-1] != '*':
                    dp[i][j] = dp[i-1][j-1] and (s[i-1] == p[j-1] or p[j-1] == '?')
                else:
                    dp[i][j] = dp[i-1][j] or dp[i][j-1]
        return dp[len(s)][len(p)]
        '''
        #version 3.0 dp 1212ms
        count = 0
        for char in p:
            if char == '*':
                count += 1
        if len(p) - count > len(s):
            return False
        dp = [[False for i in range(len(s)+1)] for j in range(len(p)+1)]
        dp[0][0] = True
        for j in range(1,len(p)+1):
            dp[j][0] = dp[j-1][0] and p[j-1] == '*'
            for i in range(1,len(s)+1):
                if p[j-1] != '*':
                    dp[j][i] = dp[j-1][i-1] and (s[i-1] == p[j-1] or p[j-1] == '?')
                else:
                    dp[j][i] = dp[j-1][i] or dp[j][i-1]
        return dp[len(p)][len(s)]
