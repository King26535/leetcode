class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        '''#version 1.0 time limit exceeded
        result = ""
        l = len(s)
        if l == 0 or l == 1:
            return l
        else:
            for i in range(l):
                temp = s[i]
                for j in range(i+1,l):
                    if s[j] in temp:
                        break
                    else:
                        temp += s[j]
                if len(temp) > len(result):
                    result = temp
            return len(result)
        '''
        '''# version 2.0
        maxlen, first, dict = 0, 0, {}
        for i in range(len(s)):
            if len(s[first:i+1]) != len(set(s[first:i+1])):
                first = dict[s[i]] + 1
            else:
                maxlen = max(maxlen, i-first+1)
            dict[s[i]] = i
        return maxlen
        '''
        # version 2.1
        maxlen, first, dict = 0, 0, {}
        for i in range(len(s)):
            if s[i] in dict and first <= dict[s[i]]:
                first = dict[s[i]] + 1
            else:
                maxlen = max(maxlen, i-first+1)
            dict[s[i]] = i
        return maxlen
