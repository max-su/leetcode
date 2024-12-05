# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack = []
        while root:
            stack.append(root)
            root = root.left
            
        
        res = None
        for _ in range(k):
            res = n = stack.pop()
            if n.right:
                n = n.right
                while n:
                    stack.append(n)
                    n = n.left
        return res.val