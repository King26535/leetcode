class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        '''
        #version 1.0 59ms
        left,right = 0,len(height)-1
        ml,mr = 0,0
        res = 0
        while left <= right:
            if ml <= mr:
                if height[left] >= ml:
                    ml = height[left]
                else:
                    res += ml - height[left]
                left += 1
            else:
                if height[right] >= mr:
                    mr = height[right]
                else:
                    res += mr - height[right]
                right -= 1
        return res
        '''
        # version 2.0 52ms
        left,right = 0,len(height)-1
        ml,mr = 0,0
        res = 0
        while left < right:
            ml = max(ml,height[left])
            mr = max(mr,height[right])
            if ml < mr:
                res += ml - height[left]
                left += 1
            else:
                res += mr - height[right]
                right -= 1
        return res
