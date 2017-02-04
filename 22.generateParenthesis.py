class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        res = []
        self.addingpar(res,'',n,0)
        return res
    
    def addingpar(self,res,s,n,m):
        if n > 0:
            self.addingpar(res,s+'(',n-1,m+1)
        if m > 0:
            self.addingpar(res,s+')',n,m-1)
        if n == 0 and m == 0:
            res.append(s)
            return
