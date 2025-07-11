class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 0: return []
        if numRows == 1: return [[1]]
        if numRows == 2: return [[1],[1,1]]
        
        results = [[1],[1,1]]
        for i in range(2,numRows):

            result = [0] * (i+1)
            prev_index_line = i-1
            prev_line = results[prev_index_line]

            result[0] = 1
            result[i] = 1
            for s in range(1,i):
                v1 = prev_line[s-1]
                v2 = prev_line[s]
                result[s] = v1 + v2

            results.append(result)

        return results

