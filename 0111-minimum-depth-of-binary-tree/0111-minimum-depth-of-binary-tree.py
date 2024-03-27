# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root: return 0
        if not root.left and not root.right:
            return 1
        mn= 10**5
        if root.left:
            mn=min(self.minDepth(root.left),mn)
        if root.right:
            mn=min(self.minDepth(root.right),mn)
       
        return mn + 1;
        