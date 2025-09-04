# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot: return True
        if not root: return False
        
        if self.same(root, subRoot): return True
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

    def same(self, node1, node2):
        if not node1:
            if not node2: return True
            return False
        if not node2:
            if not node1: return True
            return False
        
        if node1.val == node2.val:
            return self.same(node1.left, node2.left) and self.same(node1.right, node2.right)
        
        return False