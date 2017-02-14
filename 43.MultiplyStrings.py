class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        '''
        # version 1.0 89ms
        tmp1,tmp2 = 0,0
        for i in num1:
            tmp1 = 10*tmp1 + int(i)
        for i in num2:
            tmp2 = 10*tmp2 + int(i)
        tmp3 = tmp1*tmp2
        res = ''
        if tmp3 == 0:
            return '0'
        while tmp3>0:
            res = str(tmp3%10) + res
            tmp3 /= 10
        return res
        '''
        '''
        #version 2.0 475ms
        m,n = len(num1),len(num2)
        product = [0]*(m+n)
        for i in range(m-1,-1,-1):
            for j in range(n-1,-1,-1):
                temp = int(num1[i])*int(num2[j]) + product[i+j+1]
                product[i+j] += temp/10
                product[i+j+1] = temp%10
                
        res = ''
        for i in product:
            if res != '' or i != 0:
                res += str(i)
        return '0' if res == '' else res
        '''
        #version 3.0 399ms
        m,n = len(num1),len(num2)
        product = [0]*(m+n)
        for i in range(m-1,-1,-1):
            for j in range(n-1,-1,-1):
                product[i+j+1] += int(num1[i])*int(num2[j])
        carry = 0
        for i in range(m+n-1,-1,-1):
            temp = product[i] + carry
            carry = temp/10
            product[i] = temp%10
        res = ''
        for i in product:
            if res != '' or i != 0:
                res += str(i)
        return '0' if res == '' else res
