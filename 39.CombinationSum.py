class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res,temp = [],[]
        candidates.sort()
        self.comSum(candidates,target,res,temp,0)
        return res
        
    def comSum(self,candidates, target,res,temp,begin):
        if target == 0:
            res.append(temp)
            return
        for i in range(begin,len(candidates)):
            if target < candidates[i]:
                return
            else:
                self.comSum(candidates,target-candidates[i],res,temp+[candidates[i]],i)
