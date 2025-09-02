import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        max_heap = []
        for n in nums:
            heapq.heappush(max_heap,n)

            if len(max_heap)>k:
                heapq.heappop(max_heap)

        #print(max_heap)
        return max_heap[0]
