class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        for i,item in enumerate(intervals):
            if i>0 and item[0]<=intervals[i-1][1] :
                if item[1]>intervals[i-1][1]:
                    intervals[i] = [intervals[i-1][0],item[1]]
                    intervals[i-1] = 'xxx'
                else:
                    intervals[i] = intervals[i-1] 
                    intervals[i-1] = 'xxx'
        while 'xxx' in intervals:
            intervals.remove('xxx')
        return intervals