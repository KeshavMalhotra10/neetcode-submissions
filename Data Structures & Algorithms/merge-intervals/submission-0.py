class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        #intervals = [[1,3],[1,5],[6,7]]
        #overlap bc 1 <=1 and 3>1
        #sort by start so our start always is <= to the next start
        intervals.sort()
        print(intervals)
        res = []

        for start, end in intervals:
            #overlap
            if res and res[-1][1]>=start:
                res[-1][1] = max(res[-1][1], end)
            #no overlap
            else:
                res.append([start, end])
        return res

        