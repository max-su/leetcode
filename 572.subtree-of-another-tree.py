# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def is_same(p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
            if bool(p) != bool(q):
                return False
            if not p and not q:
                return True
            return p.val == q.val and is_same(p.left, q.left) and is_same(p.right, q.right)
        if is_same(root, subRoot):
            return True
        if not root:
            return False
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)