class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        s = '1'
        for i in range(2,n+1):
            s = self.count(s)
        return s
        
    def count(self,s):
        cur = '#'
        res = ''
        for i in s:
            if i != cur:
                if cur != '#':
                    res += str(count) + cur
                cur = i
                count = 1
            else:
                count += 1
        res += str(count) + cur
        return res
        
