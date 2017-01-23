class Solution(object):
    '''#version 1.0, reverse to integer
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        elif x < 10:
            return True
        else:
            temp = self.reverse(x)
            if temp > 2**31-1:
                return False
            return temp == x
        
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
        #if result >= 2**31-1:
        #    return 0
        return result if is_positive else -result
    '''
    #version 2.0, reverse to string
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        elif x < 10:
            return True
        else:
            temp = str(x)
            if int(temp[::-1]) > 2**31 - 1:
                return False
            else:
                return temp == temp[::-1]
