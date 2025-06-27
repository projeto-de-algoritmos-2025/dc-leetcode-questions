class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def balanceBST(self, root):
        def inorder(node):
            if not node:
                return []
            return inorder(node.left) + [node.val] + inorder(node.right)

        def build_balanced_bst(values, start, end):
            if start > end:
                return None

            mid = (start + end) // 2
            root = TreeNode(values[mid])

            root.left = build_balanced_bst(values, start, mid - 1)
            root.right = build_balanced_bst(values, mid + 1, end)
            return root

        sorted_values = inorder(root)
        return build_balanced_bst(sorted_values, 0, len(sorted_values) - 1)
