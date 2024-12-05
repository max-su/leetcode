# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # P is the smallest value node
        if p.val > q.val:
            p, q = q, p
        def lca(root, p, q):
            if p.val <= root.val <= q.val:
                return root
            elif root.val > p.val and root.val > q.val:
                return lca(root.left, p, q)
            return lca(root.right, p, q)
        return lca(root, p, q)