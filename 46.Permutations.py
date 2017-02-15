class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # 69ms
        res = []
        if len(nums) == 0:
            return []
        elif len(nums) == 1:
            return [nums]
        for i in range(len(nums)):
            for theother in self.permute(nums[:i]+nums[i+1:]):
                res.append([nums[i]]+theother)
        return res
