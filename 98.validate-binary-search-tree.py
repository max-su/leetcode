# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def is_valid_bst(root: TreeNode | None, l_bound: int | float, r_bound: int | float) -> bool:
            if not root:
                return True
            if root.val <= l_bound or root.val >= r_bound:
                return False
            return is_valid_bst(root.left, l_bound, root.val) and \
                   is_valid_bst(root.right, root.val, r_bound)
            
        return is_valid_bst(root, float('-inf'), float('inf'))