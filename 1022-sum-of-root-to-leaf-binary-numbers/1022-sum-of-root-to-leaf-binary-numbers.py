# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        
        def dfs(r,sm):
            if not r:
                return 0
            sm = (sm << 1) | r.val
            if not r.left and not r.right:
                return sm
            return dfs(r.left,sm)+dfs(r.right,sm)
    
        return  dfs(root,0)
        