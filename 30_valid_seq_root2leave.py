# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidSequence(self, root: TreeNode, arr: List[int]) -> bool:
        _len = len(arr)
        i = 0
        
        if root == None:
            return _len == 0
        if root.left == None and root.right == None and _len == 1:
            return root.val == arr[0]
        if root.val == arr[i]:
            i += 1
            while i < _len:
                return self.isValidSequence(root.left, arr[i:]) or self.isValidSequence(root.right, arr[i:])
            return False