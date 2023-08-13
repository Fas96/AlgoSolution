# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:  
    ans=0
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        if not root: return 0
        @cache
        def dfs(node,target):
            if not node: return 0
            if (node.val==target):self.ans+=1
            dfs(node.left,target-node.val)
            dfs(node.right,target-node.val)
        
        dfs(root, targetSum)
        self.pathSum(root.left, targetSum)
        self.pathSum(root.right, targetSum)
        return self.ans
        
        