# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
 
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        self.count = 0
        def sum(node, targetSum):
            if node is None:
                return 
            elif node.val==targetSum:
                self.count+=1
            sum(node.left, targetSum-node.val)
            sum(node.right, targetSum-node.val)
        def dfs(node, target):
            if node is None:
                return 
            sum(node, target)
            dfs(node.left, target)
            dfs(node.right,target)
        dfs(root, targetSum)
        return self.count