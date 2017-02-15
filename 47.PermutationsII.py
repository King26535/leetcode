class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # 119ms
        res = []
        prenum = None
        if len(nums) == 0:
            return []
        elif len(nums) == 1:
            return [nums]
        nums.sort()
        for i in range(len(nums)):
            if nums[i] == prenum:
                continue
            prenum = nums[i]
            for theother in self.permuteUnique(nums[:i]+nums[i+1:]):
                res.append([nums[i]]+theother)
        return res
