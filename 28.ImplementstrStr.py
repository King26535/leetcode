class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        '''#version1.0
        hl,nl = len(haystack),len(needle)
        if needle not in haystack:
            return -1
        else:
            for i in range(hl-nl+1):
                if haystack[i:i+nl] == needle:
                    return i
        '''
        #version2.0
        hl,nl = len(haystack),len(needle)
        if nl == 0:
            return 0
        for i in range(hl-nl+1):
            for j in range(nl):
                if haystack[i+j] != needle[j]:
                    break
                elif j == nl - 1:
                    return i
        return -1
                
