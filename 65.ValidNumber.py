class Solution(object):
    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """
        state = [
            {},
            {'blank':1, 'sign':2, 'number':3, 'dot':4},#space
            {'number':3, 'dot':4},#sign
            {'number':3, 'dot':5, 'e':6, 'blank':9},#digit ' 111' or ' +/-111'
            {'number':5},#dot
            {'number':5, 'e':6, 'blank':9},#digit.(digit)   (digit).digit ' 111.11' or ' +/-111.11' or ' .11' or ' +/-.11'
            {'sign':7, 'number':8},# e
            {'number':8},#e +/-
            {'number':8, 'blank':9},#e-6, e6' 111e' or ' +/-111e' or ' 111.11e' or ' +/-111.11e' or ' .11e' or ' +/-.11e' + '+/-11' or '11'
            {'blank':9}]#the rest is space ' xxxx   '
        curstate = 1
        for char in s:
            if char == ' ':
                char = 'blank'
            elif char in '+-':
                char = 'sign'
            elif char in '0123456789':
                char = 'number'
            elif char == '.':
                char = 'dot'
            if char not in state[curstate]:
                return False
            curstate = state[curstate][char]
        if curstate not in [3,5,8,9]:
            return False
        return True
        
