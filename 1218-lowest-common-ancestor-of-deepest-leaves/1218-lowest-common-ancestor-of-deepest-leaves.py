# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def treeHeight(node):
            if not node:
                return 0
            return 1+max(treeHeight(node.left),treeHeight(node.right))
        def dfs(node,maxH,L):
            if not node:
                return None
            if maxH-1==L:
                return node
            left=dfs(node.left,maxH,L+1)
            right=dfs(node.right,maxH,L+1)
            if left and right:
                return node
            return left if left else right
        maxi=treeHeight(root)
        return dfs(root,maxi,0)