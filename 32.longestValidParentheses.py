class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        last = -1
        temp = []
        maxlen = 0
        if len(s) < 2:
            return 0
        for i in range(len(s)):
            if s[i] == '(':
                temp.append(i)
            else:
                if temp == []:
                    last = i
                else:
                    temp.pop()
                    if temp == []:
                        maxlen = max(maxlen,i - last)
                    else:
                        maxlen = max(maxlen,i - temp[-1])
        return maxlen
