# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def distributeCoins(self, r: Optional[TreeNode]) -> int:
        def f(n):
            if n:
                l, r = f(n.left), f(n.right)
                c = n.val + l[0] + r[0] - 1
                return (c, l[1] + r[1] + abs(c))
            return (0, 0)
        
        return f(r)[1]