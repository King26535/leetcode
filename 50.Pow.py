class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        '''
        #version 1.0 maximum recursion depth exceeded
        if n == 0:
            return 1
        elif n > 0:
            return self.myPow(x,n-1)*x
        else:
            return self.myPow(x,n+1)/x
        '''
        
        #version 2.0
        if n == 0:
            return 1
        if n < 0:
            n = -n
            x = 1/x
        if n%2 == 0:
            return self.myPow(x*x, n/2)
        else:
            return self.myPow(x*x, n/2) * x
