# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        if not root: return 0
        
        q=deque([(root,1)])
        ls={}
        while q:
            n,l=q.popleft()
            ls[l]=ls.get(l,0)+n.val
            if n.left: q.append((n.left,l+1))
            if n.right: q.append((n.right,l+1))
        return max(ls,key=ls.get)
