# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        def dfs(H):
            if not H: return True
            l,r=dfs(H.left),dfs(H.right)
            if l: H.left=None
            if r: H.right=None
            return l and r and H.val==target
        return root if not dfs(root) else None
        