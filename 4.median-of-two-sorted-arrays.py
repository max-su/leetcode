import heapq


class Solution:
    def findMedianSortedArrays(self, nums0: List[int], nums1: List[int]) -> float:
        def heaps_append(v, max_heap, min_heap):
            heapq.heappush(min_heap, v)
            if len(min_heap) - len(max_heap) > 1:
                v = heapq.heappop(min_heap)
                heapq.heappush(max_heap, v * -1)

        max_heap, min_heap = [], []
        i = j = 0
        while i < len(nums0) or j < len(nums1):
            val0 = nums0[i] if i < len(nums0) else float('inf')
            val1 = nums1[j] if j < len(nums1) else float('inf')
            if val0 < val1:
                heaps_append(val0, max_heap, min_heap)
                i += 1
            else:
                heaps_append(val1, max_heap, min_heap)
                j += 1

        if (len(max_heap) + len(min_heap)) % 2 == 1:
            return min_heap[0]
        return (min_heap[0] - max_heap[0]) // 2