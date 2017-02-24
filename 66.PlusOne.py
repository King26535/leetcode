class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        '''
        #version 1.0
        c = 1
        for i in range(len(digits)-1,-1,-1):
            temp = digits[i] + c
            digits[i] = temp%10
            c = temp/10
            if c == 0:
                return digits
        if c:
            return [1] + digits
        '''
        #version 2.0
        for i in range(len(digits)-1,-1,-1):
            if digits[i] < 9:
                digits[i] += 1
                return digits
            else:
                digits[i] = 0
        return [1] + digits
