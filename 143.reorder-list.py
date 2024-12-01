# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head or not head.next:
            return

        dummy_head = slow = fast = ListNode(next=head)
        while fast.next is not None:
            slow = slow.next
            # F 1 2
            if fast.next.next:
                fast = fast.next.next
            else:
                fast = fast.next

        # Divide the Linkedlist into two halves
        first_half_head = dummy_head.next
        first_half_tail = slow
        second_half_head = slow.next
        second_half_tail = fast
        slow.next = None
        
        # Reverse the second half
        def reverse(head):
            prev = temp = None
            while head:
                temp = head.next
                head.next = prev
                prev, head = head, temp
            return prev
        
        reverse(second_half_head)
        second_half_head, second_half_tail = second_half_tail, second_half_head

        # Stitch the two back together, odd elements 2n + 1, |first_half| = n + 1
        turn_first = True
        node1, node2 = first_half_head, second_half_head
        d_head = tail = ListNode()
        while node1 or node2:
            if turn_first:
                tail.next = node1
                node1 = node1.next
            else:
                tail.next = node2
                node2 = node2.next

            turn_first = not turn_first
            tail = tail.next
            tail.next = None

        return d_head.next