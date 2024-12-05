# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def is_good(root: TreeNode, max_seen: int) -> int:
            # Node is good if in the path from root to X, there are no nodes with a value greater than X
            if not root:
                return 0
            
            res = 1 if root.val >= max_seen else 0
            return res + is_good(root.left, max(max_seen, root.val)) + \
                       + is_good(root.right, max(max_seen, root.val))

        return is_good(root, float('-inf'))