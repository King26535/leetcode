# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[Interval]
        :type newInterval: Interval
        :rtype: List[Interval]
        """
        '''
        #version 1.0
        intervals += [newInterval]
        res = []
        for i in sorted(intervals,key = lambda x: x.start):
            if res and i.start <= res[-1].end:
                res[-1].end = max(res[-1].end, i.end)
            else:
                res += [i]
        return res
        '''
        #version 2.0
        left, right = [], []
        s, e = newInterval.start, newInterval.end
        for i in intervals:
            if i.end < s:
                left += [i]
            elif i.start > e:
                right += [i]
            else:
                s = min(s, i.start)
                e = max(e, i.end)
        return left + [Interval(s,e)] + right
