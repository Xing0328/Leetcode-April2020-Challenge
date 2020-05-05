# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        self.res = 0
        def d_helper(root):
            if not root:
                return 0
            left = d_helper(root.left)
            right = d_helper(root.right)
            self.res = max(self.res, left+right)
            return 1 + max(left, right)
        d_helper(root)
        return self.res
        