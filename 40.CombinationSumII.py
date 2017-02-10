class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res,temp = [],[]
        candidates.sort()
        self.comSum2(candidates,target,res,temp,0)
        return res
        
    def comSum2(self,candidates, target,res,temp,begin):
        if target == 0:
            res.append(temp)
            return
        for i in range(begin,len(candidates)):
            if i != begin and candidates[i] == candidates[i-1]:
                continue
            if target < candidates[i]:
                return
            else:
                self.comSum2(candidates,target-candidates[i],res,temp+[candidates[i]],i+1)
