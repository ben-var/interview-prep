import heapq
from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        heap = []
        c = Counter(nums)
        for n in c.keys():
            heap.append((-c[n], n)) # negative for min-heap --> max-heap
        
        heapq.heapify(heap)
        
        res = []
        for i in range(k):
            res.append(heapq.heappop(heap)[1])
        return res