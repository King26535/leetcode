class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        sign, i, result = True, 0, 0
        if len(str) == 0:
            return 0
        while str[i] == ' ':
            i += 1
        if str[i] == '-':
            sign = False
            i += 1
        elif str[i] == '+':
            i += 1
        # case: input: "1"   
        while i < len(str) and str[i] in "0123456789":
            result = 10*result + int(str[i])
            i += 1
        if result > 2**31 - 1:
            return 2**31-1 if sign else -2**31
        return result if sign else -result
