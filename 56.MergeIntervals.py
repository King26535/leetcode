# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        '''
        #version 1.0
        if len(intervals) <= 1:
            return intervals
        intervals.sort(key = lambda x:x.start)
        res = [intervals[0]]
        for i in range(1,len(intervals)):
            if res[-1].end < intervals[i].start:
                res.append(intervals[i])
            else:
                res[-1].end = max(res[-1].end,intervals[i].end)
        return res
        '''
        #version2.0
        res = []
        for i in sorted(intervals, key = lambda x:x.start):
            if res and i.start <= res[-1].end:
                res[-1].end = max(res[-1].end, i.end)
            else:
                res += [i]
        return res
