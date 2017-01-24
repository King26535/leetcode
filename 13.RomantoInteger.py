class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        
        "DCXXI" 621
        """
        init = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        result = 0
        temp = 2**30
        for char in s:
            result = result + init[char] if temp >= init[char] else result + init[char] - 2*temp
            temp = init[char]
        return result
