# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root: return 0
        curr_depth = 0
        queue = deque()
        queue.append(root)

        while len(queue) > 0:
            for i in range(len(queue)):
                current = queue.popleft()
                if current.left: queue.append(current.left)
                if current.right: queue.append(current.right)
            
            curr_depth += 1

        return curr_depth