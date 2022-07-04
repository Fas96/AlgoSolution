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
            if nh:
                ls.add(nh.val)
                dfs(nh.left)
                dfs(nh.right)

        dfs(root)
        mins,ans=root.val,float("inf")
        for v in ls:
            if mins<v<ans:
                ans=v
        return  ans if ans<float("inf") else -1
            
        