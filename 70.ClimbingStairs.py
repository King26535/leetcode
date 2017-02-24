class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        #version 1.0 56ms
        def Cnk(n,k):
            res = 1.0
            for i in xrange(1,k+1):
                res = res*(n-k+i)/i
            return int(res)
        two = (n+1)/2 - 1
        res = 1 if n%2 == 1 else 2
        for i in xrange(1,two+1):
            res += Cnk(n-i,i)
        return res
        
        #version 2.0 75ms
        '''
        if n == 0:
            return 0
        if n == 1:
            return 1
        if n == 2:
            return 2
        one_step_before = 2
        two_step_before = 1
        all_ways = 0
        for i in range(2,n):
            all_ways = one_step_before + two_step_before
            two_step_before = one_step_before
            one_step_before = all_ways
        return all_ways
        '''
        #version 3.0 TLE
        '''
        if n == 1:
            return 1
        elif n == 2:
            return 2
        else:
            return self.climbStairs(n-1) + self.climbStairs(n-2)
        '''
        #version 4.0 88ms
        '''
        if n == 1:
            return 1
        res = [0]*n
        res[0],res[1] = 1,2
        for i in xrange(2,n):
            res[i] = res[i-1] + res[i-2]
        return res[-1]
        '''
        
