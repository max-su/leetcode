# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        d_head = tail = ListNode()
        carryover = False
        while l1 or l2 or carryover:
            l1_val = l1.val if l1 else 0
            l2_val = l2.val if l2 else 0
            curr_sum = (1 if carryover else 0) + l1_val + l2_val
            carryover = curr_sum >= 10
            tail.next = ListNode(curr_sum % 10)
            tail = tail.next
            
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        
        return d_head.next