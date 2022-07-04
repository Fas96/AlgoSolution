# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findSecondMinimumValue(self, root: Optional[TreeNode]) -> int:
        ls=set()
        def dfs(nh):
            if not nh:
                return
            if nh.left is not None and nh.right is not None:
                if nh.left.val is not nh.right.val:
                    ls.add(min(nh.right.val,nh.left.val))
                    ls.add(max(nh.right.val,nh.left.val))
                else:
                    ls.add(min(nh.left.val,nh.right.val))
            dfs(nh.left)
            dfs(nh.right)
        dfs(root)
        ls=list(sorted(ls))
        return ls[1] if len(ls)>=2 else -1
            
        