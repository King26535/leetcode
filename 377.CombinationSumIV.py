class Solution(object):
    def combinationSum4(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if nums == []:
            return 0
        dp = [0]*(target + 1)
        dp[0] = 1
        for i in range(1,target+1):
            for x in nums:
                if x <= i:
                    dp[i] += dp[i-x]
        return dp[target]
