import heapq

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        min_heap = []
        # i is used for tiebreaking n
        for i, n in enumerate(lists):
            if n is None:
                continue
            heapq.heappush(min_heap, (n.val, i, n))
            
        d_head = tail = ListNode()
        while min_heap:
            _, i, n = heapq.heappop(min_heap)
            if n.next:
                heapq.heappush(min_heap, (n.next.val, i, n.next))
                
            tail.next = n
            tail = tail.next
            tail.next = None
        
        return d_head.next