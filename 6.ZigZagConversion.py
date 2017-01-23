class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        a = []
        result = ""
        for i in range(numRows):
            a.append([])
        i, flag = 0, True
        for item in s:
            a[i].append(item)
            if flag:
                if i < numRows-1:
                    i += 1
                else:
                    i -= 1
                    flag = False
            else:
                if i > 0:
                    i -= 1
                else:
                    i += 1
                    flag = True
        for i in range(numRows):
            result += ''.join(a[i])
        return result
        
