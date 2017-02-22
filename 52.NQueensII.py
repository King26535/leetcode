class Solution(object):
    def totalNQueens(self, n):
        """
        :type n: int
        :rtype: int
        """
        def dfs(queens,xy_dif,xy_sum):
            l = len(queens)
            if l == n:
                res.append(queens)
            for i in range(n):
                if i not in queens and i-l not in xy_dif and i+l not in xy_sum:
                    dfs(queens+[i],xy_dif+[i-l],xy_sum+[i+l])
        res = []
        dfs([],[],[])
        return len(res)
