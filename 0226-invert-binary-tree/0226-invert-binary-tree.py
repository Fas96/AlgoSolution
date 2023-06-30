# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return root
        q = [root]
        while q:
            c = q.pop(0)
            c.left,c.right=c.right,c.left
            if c.left:
                q.append(c.left)
            if c.right:
                q.append(c.right)
        return root