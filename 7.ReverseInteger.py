class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        is_positive = True if x > 0 else False
        result = 0
        temp = abs(x)
        while temp > 0:
            result = 10*result + temp%10
            temp /= 10
        #overflow return 0
        if result >= 2**31-1:
            return 0
        return result if is_positive else -result
