# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        v_to_inorder_idx = {v: i for i, v in enumerate(inorder)}
        def build_tree(p: int, l: int, r: int) -> TreeNode | None:
            if l > r:
                return None 
            node = TreeNode(preorder[p])
            inorder_idx = v_to_inorder_idx[node.val]
            # 0 1 2 3

            left_size = inorder_idx - l

            node.left = build_tree(p + 1, l, inorder_idx - 1)
            node.right = build_tree(p + left_size + 1,inorder_idx + 1, r)
            
            return node

        return build_tree(0, 0, len(inorder) - 1)