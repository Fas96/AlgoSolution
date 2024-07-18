# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countPairs(self, root: TreeNode, distance: int) -> int:
        def depSearch(n):
            if not n:return []
            if not n.left and not n.right:return [1]
            ld=depSearch(n.left)
            rd=depSearch(n.right)
            nonlocal ans
            ans += sum(1 for l in ld for r in rd if l + r <= distance)
            return [d+1 for d in ld+rd if d+1<=distance]
        ans=0
        depSearch(root)
        return ans
        