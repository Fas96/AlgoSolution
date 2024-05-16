# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def evaluateTree(self, root: Optional[TreeNode]) -> bool:
        if not root: return True
        
        def dfs(head):
            if not head: return True
            if not head.left and not head.right:
                return True if head.val==1 else False
            if head.val==2:
                return dfs(head.left) or dfs(head.right)
            elif head.val==3:
                return  dfs(head.left) and dfs(head.right)
        
        
        return dfs(root)
        