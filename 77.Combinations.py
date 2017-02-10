class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        '''
        #version 1.0 TLE
        def dfs(start,temp):
            if self.count == k:
                res.append(temp)
                return
            for i in range(start, n+1):
                self.count += 1
                dfs(i+1,temp+[i])
                self.count -= 1
                
        res = []
        self.count = 0
        dfs(1,[])
        return res
        '''
        
        # version 2.0
        if k == 1:
            return [[i] for i in range(1,n+1)]
        res = []
        if n > k:
            res = [r + [n] for r in self.combine(n-1,k-1)] + self.combine(n-1,k)
        else:
            res = [r + [n] for r in self.combine(n-1,k-1)]
        return res
        
        ''' TLE
        # version 3.0
        res = []
        self.rec(res, 0, n, k, [])
        return res
        
    def rec(self, res, i, n, k, temp):
        if k == 0:
            res.append(temp)
            return
        for j in range(i + 1, n + 1):
            self.rec(res, j, n, k - 1, temp + [j])
        '''
        
                
