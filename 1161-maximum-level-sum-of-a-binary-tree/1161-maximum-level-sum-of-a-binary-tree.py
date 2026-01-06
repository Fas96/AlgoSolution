# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        ls = {}
        
        def dfs(node, level):
            if not node:
                return
            ls[level] = ls.get(level, 0) + node.val
            dfs(node.left, level + 1)
            dfs(node.right, level + 1)
        dfs(root, 1)
        return max(ls, key=ls.get)
