class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        res, temp, skip = '', [], ['','.','..']
        for item in path.split('/'):
            if item == '..' and temp != []:
                temp.pop()
            elif item not in skip:
                temp += [item]
        for item in temp:
            res += '/' + item
        return '/' if res == '' else res
