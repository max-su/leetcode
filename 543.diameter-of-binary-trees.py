# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.res = 0
        def depth(root: Optional[TreeNode]) -> int:
            if not root:
                return 0
            # Returns the length of the longest path that terminates at the root, depth
            left_depth = depth(root.left)
            right_depth = depth(root.right)
            self.res = max(1 + left_depth + right_depth, self.res)
            return 1 + max(left_depth, right_depth)
            
        depth(root)
        
        return self.res - 1