class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        left, right = 0, 0
        for i in range(len(s)-1):
            len1 = self.center(s, i, i)
            len2 = self.center(s, i, i+1)
            maxlen = max(len1, len2)
            if maxlen > right-left+1:
                left = i - (maxlen-1)/2
                right = i + maxlen/2
        return s[left:right+1]
        
    def center(self, s, left, right):
        result = 0
        while left >= 0 and right < len(s) and s[left]==s[right]:
            result = right-left+1
            left -= 1
            right += 1
        return result
