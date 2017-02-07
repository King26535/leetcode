class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        sign = False
        if (dividend < 0 and divisor > 0) or (dividend > 0 and divisor < 0):
            sign = True
        
        a,b,res = abs(dividend),abs(divisor),0
        
        if b == 0 or (a > 2**31-1 and divisor == -1):
            return 2**31-1

        while a >= b:
            temp,multiple = b,1
            while a >= (temp << 1):
                temp = temp << 1
                multiple = multiple << 1
            a -= temp
            res += multiple
        res = -res if sign else res
        return res
