import heapq
import collections


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #  K most frequent elements
        n_to_freq = collections.Counter(nums)
        min_heap = []
        i = 0
        for n, freq in n_to_freq.items():
            heapq.heappush(min_heap, (freq, n, i))
            if len(min_heap) > k:
                heapq.heappop(min_heap)

        return [x[1] for x in heapq.nlargest(k, min_heap)]
