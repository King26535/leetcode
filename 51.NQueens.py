class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
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
        return [['.'*i + 'Q' + '.'*(n-1-i) for i in row] for row in res]
            
