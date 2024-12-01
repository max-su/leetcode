"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None

        d_head = ListNode(next=head)

        # node -> deepcopy -> node.next -> node.next.deepcopy ->
        curr = d_head.next
        while curr:
            temp = curr.next

            curr.next = Node(curr.val)
            # Set to deep copied next later
            curr.next.next = temp
            # Set to deep copied random later
            curr.next.random = None
            
            curr = temp
        
        # Set all random pointers to the deep copied random equivalent
        curr = d_head.next
        while curr:
            temp = curr.next.next
            
            # Set the deep copied node's random field
            if curr.random:
                curr.next.random = curr.random.next

            curr = temp
        
        # Seperate the two lists
        curr = d_head.next
        res = curr.next
        while curr:
            temp = curr.next.next
            deep_copy = curr.next
            
            # Modify both next pointers to next respective node
            if temp:
                deep_copy.next = temp.next
            curr.next = temp
            curr = curr.next
            
        return res
        
        
        
        # HashMap Implementation
        # if not head:
        #     return None
        # d_head = ListNode(next=head)
        # curr = d_head.next

        # # Make deep copies of the nodes
        # node_to_copy = {}
        # while curr:
        #     node_to_copy[curr] = ListNode(curr.val)
        #     curr = curr.next
        
        # # Assign pointers
        # curr = d_head.next
        # while curr:
        #     # Save the next to continue iterating through old list
        #     temp = curr.next

        #     if curr.next:
        #         node_to_copy[curr].next = node_to_copy[curr.next]
        #     if curr.random:
        #         node_to_copy[curr].random = node_to_copy[curr.random]
        #     else:
        #         node_to_copy[curr].random = None 
            
        #     curr = temp

        # return node_to_copy[head]