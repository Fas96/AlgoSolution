# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        
        if not root1:
            return root2
        if not root2:
            return root1
        q = [(root1, root2)]
        while q:
            f, s = q.pop(0)
            f.val += s.val
            if f.left and s.left:
                q.append((f.left, s.left))
            elif s.left:
                f.left = s.left
            if f.right and s.right:
                q.append((f.right, s.right))
            elif s.right:
                f.right = s.right

        return root1
         
        