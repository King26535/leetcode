class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        #version 1.0 good
        init = {
            ')':'(',
            ']':'[',
            '}':'{'
            }
        temp = []
        for i in s:
            if i in '{([':
                temp.append(i)
            elif temp == []:
                return False
            else:
                if temp[-1] == init[i]:
                    temp.pop()
                else:
                    return False
        return temp == []
        '''
        #version 2.0 bad
        l = len(s)
        temp = s.replace('{}','').replace('()','').replace('[]','')
        while l != len(temp):
            l = len(temp)
            temp = temp.replace('{}','').replace('()','').replace('[]','')
        return temp == ''
        '''
