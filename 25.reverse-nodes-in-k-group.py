# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        def reverse(head: Optional[ListNode]):
            if not head:
                return None, None

            new_tail = head
            prev, temp = None, None
            while head:
                temp = head.next
                head.next = prev
                
                prev, head = head, temp

            return prev, new_tail
            
        if not head or k <= 1:
            return head

        dummy_head = s = f = ListNode(next=head)
        p = dummy_head

        while True:
            for _ in range(k):
                if f.next == None:
                    return dummy_head.next
                f = f.next

            # Prev and n of k-group
            n = f.next
            head, tail = s.next, f
            tail.next = None
            new_head, new_tail = reverse(head)

            # Connect the previous portion of the LL to the reverse-group
            p.next = new_head
            p = new_tail
            
            # Connect the current k-group to the rest of the LL to process
            new_tail.next = n
            
            s, f = new_tail, new_tail
        return dummy_head.next