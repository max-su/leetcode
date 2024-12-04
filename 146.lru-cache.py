class ListNode:
    def __init__(self, key, value, next=None, prev=None):
        self.next = next
        self.prev = prev
        self.key = key
        self.value = value

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.d_head = ListNode(-1,-1)
        self.d_tail = ListNode(-1,-1)
        self.d_head.next, self.d_tail.prev = self.d_tail, self.d_head
        self.key_to_node = {}
        
    def _move_to_head(self, node: ListNode):
        p, n = node.prev, node.next
        
        # Detatch the node from the linkedlist
        p.next, n.prev = n, p
        node.prev, node.next = None, None

        # Set node as head
        p, n = self.d_head, self.d_head.next
        p.next, n.prev = node, node
        node.prev, node.next = p, n

    def get(self, key: int) -> int:
        if key not in self.key_to_node:
            return -1
        node = self.key_to_node[key]
        self._move_to_head(node)
        
        return node.value
        
    def put(self, key: int, value: int) -> None:
        if key in self.key_to_node:
            node = self.key_to_node[key]
            self._move_to_head(node)
            node.value = value
        else:
            # Add to the hashmap and appendleft to the deque
            node = ListNode(key, value)
            self.key_to_node[key] = node

            p, n = self.d_head, self.d_head.next
            p.next, n.prev = node, node
            node.prev, node.next = p, n
            
            # Remove the tail node from the LL
            if len(self.key_to_node) > self.capacity:
                tail = self.d_tail.prev
                p, n = tail.prev, tail.next

                p.next, n.prev = n, p
                tail.prev, tail.next = None, None
                
                del self.key_to_node[tail.key]


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)