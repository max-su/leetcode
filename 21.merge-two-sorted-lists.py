# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, lst0: Optional[ListNode], lst1: Optional[ListNode]) -> Optional[ListNode]:
        d_head = tail = ListNode()
        while lst0 or lst1:
            val0 = lst0.val if lst0 else float('inf')
            val1 = lst1.val if lst1 else float('inf')
            if val0 < val1:
                tail.next = lst0
                lst0 = lst0.next
            else:
                tail.next = lst1
                lst1 = lst1.next

            tail = tail.next
            tail.next = None

        return d_head.next