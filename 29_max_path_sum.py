# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        self.ans = float(-inf)
        def search(root):
            if root is None:
                return 0
            leftMax = search(root.left)
            rightMax = search(root.right)
            self.ans = max(max(leftMax, 0) + max(rightMax, 0) + root.val, self.ans)
            return max(leftMax, rightMax, 0) + root.val
        search(root)
        return self.ans
