class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 62ms
        last,cur,res = 0,0,0
        for i in range(len(nums)):
            if last < i:
                last = cur
                res += 1
            cur = max(cur,nums[i]+i)
        return res
