class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def constructFromPrePost(self, preorder, postorder):
        pos_map = {val: i for i, val in enumerate(postorder)}

        def build_tree(pre_start, pre_end, post_start, post_end):
            if pre_start > pre_end:
                return None

            root_val = preorder[pre_start]
            root = TreeNode(root_val)

            if pre_start == pre_end:
                return root

            left_root_val = preorder[pre_start + 1]
            left_root_pos = pos_map[left_root_val]
            left_size = left_root_pos - post_start + 1
            root.left = build_tree(
                pre_start + 1, pre_start + left_size, post_start, left_root_pos
            )

            root.right = build_tree(
                pre_start + left_size + 1, pre_end, left_root_pos + 1, post_end - 1
            )

            return root

        return build_tree(0, len(preorder) - 1, 0, len(postorder) - 1)
