# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        if not root: return 0
        self.res = 0

        def dfs(node: TreeNode, path: str):
            if not node.left and not node.right:
                self.res += int(path + str(node.val))
                return
            if node.left:
                dfs(node.left, path + str(node.val))
            if node.right:
                dfs(node.right, path + str(node.val))

        dfs(root, '')
        return self.res