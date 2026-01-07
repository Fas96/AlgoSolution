# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        MOD = 10**9 + 7
        def totalTree(node):
            if not node:
                return 0
            return node.val+totalTree(node.left)+totalTree(node.right)
        totalSumofTree=totalTree(root)
        self.maxAns=0
        def dfs(node):
            if not node: return 0
            ls=dfs(node.left)
            rs=dfs(node.right)
            ss = node.val + ls + rs
            otherSizeSum=totalSumofTree-ss
            self.maxAns=max(otherSizeSum*ss,self.maxAns)
            return ss
        dfs(root)
        return self.maxAns %MOD