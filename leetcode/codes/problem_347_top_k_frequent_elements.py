import heapq
from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count_element = defaultdict(int)

        for n in nums:
            count_element[n] += 1
        
        #print(count_element)

        result_index = []
        for count in count_element.values():
            heapq.heappush(result_index,count)

            if len(result_index)>k:
                heapq.heappop(result_index)
        
        #print(result_index)
        result = []
        for index in result_index:
            for k,v in count_element.items():
                if v == index and k not in result:
                    result.append(k)
        return result
