class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        '''
        #version 1.0 72ms
        dict = {
            '000': '00',
            '001': '01',
            '010': '01',
            '100': '01',
            '011': '10',
            '101': '10',
            '110': '10',
            '111': '11'}
        res = ''
        m = len(a)
        n = len(b)
        c = '0'
        if m > n:
            b = '0'*(m-n) + b
            l = m
        else:
            a = '0'*(n-m) + a
            l = n
        for i in range(l-1,-1,-1):
            res = dict[a[i]+b[i]+c][1] + res
            c = dict[a[i]+b[i]+c][0]
        if c == '0':
            return res
        else:
            return c + res
        '''
        #version 2.0 72ms
        if len(a) == 0:
            return b
        if len(b) == 0:
            return a
        if a[-1] == '1' and b[-1] == '1':
            return self.addBinary(self.addBinary(a[:-1],b[:-1]),'1') + '0'
        if a[-1] == '0' and b[-1] == '0':
            return self.addBinary(a[:-1],b[:-1]) + '0'
        else:
            return self.addBinary(a[:-1],b[:-1]) + '1'
