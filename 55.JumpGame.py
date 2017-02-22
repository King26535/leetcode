class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        l = len(nums)
        cur,G,last = 0,0,0
        for i in range(l):
            cur = nums[i] + i
            if last < i:
                return False
            else:
                G = max(G,cur)
                last = G
                if G >= l-1:
                    return True
        return True
