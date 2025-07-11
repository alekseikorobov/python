class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        intervals = sorted(intervals, key=lambda x:x[0])
        result_intervals = []
        a, b = intervals[0]
        for i in range(1, len(intervals)):
            a_new, b_new = intervals[i]

            if a_new <= b:
                if b_new>b:
                    b = b_new
            else:
                result_intervals.append([a, b])
                a = a_new
                b = b_new
        result_intervals.append([a, b])
        return result_intervals

#NlogN + N, mem=O(N)