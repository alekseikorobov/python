class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        
        intervals.append(newInterval)
        intervals = sorted(intervals,key=lambda x:x[0])

        a_curr, b_curr = intervals[0]
        result = []
        for i in range(1,len(intervals)):
            a, b = intervals[i]
            if a <= b_curr:
                if b > b_curr:
                    b_curr = b
            else:
                result.append([a_curr, b_curr])
                a_curr, b_curr = a, b
        
        result.append([a_curr, b_curr])

        return result
