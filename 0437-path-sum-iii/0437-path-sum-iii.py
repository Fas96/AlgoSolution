# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution: 
    ans = 0
    def dfs(self, root, target):
        if (not root): return
        if (root.val == target): self.ans += 1
        self.dfs(root.left, target - root.val)
        self.dfs(root.right, target - root.val)

    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        if (not root): return 0
        self.dfs(root, targetSum)
        self.pathSum(root.left, targetSum)
        self.pathSum(root.right, targetSum)
        return self.ans