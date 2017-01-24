class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        '''#version 1.0
        maxarea = 0
        for i in range(len(height)-1):
            for j in range(i+1, len(height)):
                maxarea = max(maxarea, (j-i)*min(height[i],height[j]))
        return maxarea
        '''
        #version 2.0
        maxarea = 0
        l,r = 0,len(height)-1
        while l < r:
            maxarea = max(maxarea, (r-l)*min(height[l],height[r]))
            if height[l] > height[r]:
                r -= 1
            else:
                l += 1
        return maxarea
