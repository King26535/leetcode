class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        res,temp = [],[]
        candidates = range(1,10)
        self.comSum3(candidates,n,res,temp,0,k)
        return res
        
    def comSum3(self,candidates, target,res,temp,begin,k):
        if target == 0 and len(temp) == k:
            res.append(temp)
            return
        for i in range(begin,len(candidates)):
            if target < candidates[i]:
                return
            else:
                self.comSum3(candidates,target-candidates[i],res,temp+[candidates[i]],i+1,k)
