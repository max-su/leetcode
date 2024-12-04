from typing import *

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def is_balanced(root: Optional[TreeNode]) -> Tuple[int, bool]:
            if not root:
                return (0, True)
            left_height, left_bal = is_balanced(root.left)
            right_height, right_bal = is_balanced(root.right)
            
            depth = 1 + max(left_height, right_height)
            is_bal = left_bal and right_bal and abs(left_height - right_height) <= 1
            return (depth, is_bal)
        return is_balanced(root)[1]