# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root: return False
        self.res = False

        def dfs(node: TreeNode, path: int):
            if not node.left and not node.right:
                if path + node.val == targetSum:
                    self.res = True
                return
            if node.left:  dfs(node.left, path + node.val)
            if node.right: dfs(node.right, path + node.val)

        dfs(root, 0)
        return self.res