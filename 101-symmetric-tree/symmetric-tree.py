# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root: return True
        return self.checkOpposite(root.left, root.right)
    def checkOpposite(self, left, right):
        if left is None and right is None: return True
        if (left is None and right is not None) or (right is None and left is not None) or left.val != right.val: return False
        return self.checkOpposite(left.left, right.right) and self.checkOpposite(left.right, right.left)