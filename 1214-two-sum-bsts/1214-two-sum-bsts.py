# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def twoSumBSTs(self, root1: Optional[TreeNode], root2: Optional[TreeNode], target: int) -> bool:
        r1Vals=[]
        r2Vals=[]
        g=root1
        def gv(root,v):
            if not root:
                return
            v.append(root.val)
            if root.left:
                gv(root.left,v)
            if root.right:
                gv(root.right,v)
            return v
        gv(root1,r1Vals)
        gv(root2,r2Vals)
        for x in r1Vals:
            if target-x in r2Vals:
                return True
        return False
        