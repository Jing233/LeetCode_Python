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
        res = []
        intervals = sorted(intervals, key=lambda x: x.start)
        i = 0
        while i < len(intervals):
            temp = Interval(intervals[i].start, intervals[i].end)
            while i + 1 < len(intervals) and intervals[i + 1].start <= temp.end:
                temp.end = max(temp.end, intervals[i + 1].end)
                i += 1
            res.append(temp)
            i += 1
        return res
            