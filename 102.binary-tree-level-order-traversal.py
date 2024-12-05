import collections

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        q = collections.deque([(0, root)])
        res = []
        while q:
            height, node = q.popleft()
            # Greater height than the last level in res
            if not res or height > res[-1][0]:
                res.append((height, []))
            res[-1][1].append(node.val)
            
            if node.left:
                q.append((height + 1, node.left))
            if node.right:
                q.append((height + 1, node.right))
            
        return [x[1] for x in res]